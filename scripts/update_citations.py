#!/usr/bin/env python3
"""Refresh citation counts in the Jekyll data files using OpenAlex."""

from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PATH = ROOT / "_data" / "publications.yml"
PROFILE_PATH = ROOT / "_data" / "profile.yml"
OPENALEX_WORKS_URL = "https://api.openalex.org/works"
REQUEST_DELAY_SECONDS = 0.2
MIN_MATCH_SCORE = 0.78


def normalize_title(title: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", title.casefold()).split())


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return yaml.safe_load(file)


def dump_yaml(path: Path, data: Any) -> None:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000)
    path.write_text(text, encoding="utf-8")


def build_headers() -> dict[str, str]:
    user_agent = os.getenv(
        "OPENALEX_USER_AGENT",
        "academic-homepage-citation-updater/1.0",
    )
    return {"User-Agent": user_agent}


def openalex_query(params: dict[str, str]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(f"{OPENALEX_WORKS_URL}?{query}", headers=build_headers())
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def collect_candidates(title: str, year: int | None) -> list[dict[str, Any]]:
    queries = []
    if year is not None:
        queries.append({"search": title, "filter": f"publication_year:{year}", "per-page": "5"})
    queries.append({"search": title, "per-page": "5"})

    results_by_id: dict[str, dict[str, Any]] = {}
    for params in queries:
        mailto = os.getenv("OPENALEX_MAILTO")
        if mailto:
            params = {**params, "mailto": mailto}
        payload = openalex_query(params)
        for item in payload.get("results", []):
            work_id = item.get("id") or item.get("display_name") or repr(item)
            results_by_id[work_id] = item
        time.sleep(REQUEST_DELAY_SECONDS)
    return list(results_by_id.values())


def extract_arxiv_id(url: str | None) -> str | None:
    if not url:
        return None
    match = re.search(r"arxiv\.org/abs/([0-9]+\.[0-9]+)", url)
    return match.group(1) if match else None


def candidate_score(publication: dict[str, Any], candidate: dict[str, Any]) -> float:
    title = normalize_title(publication["title"])
    candidate_title = normalize_title(candidate.get("display_name", ""))
    score = SequenceMatcher(None, title, candidate_title).ratio()

    if title == candidate_title:
        score += 1.0

    pub_year = publication.get("year")
    cand_year = candidate.get("publication_year")
    if pub_year is not None and cand_year is not None:
        if pub_year == cand_year:
            score += 0.12
        elif abs(pub_year - cand_year) > 1:
            score -= 0.2

    arxiv_id = extract_arxiv_id(publication.get("url"))
    if arxiv_id:
        haystacks = []
        doi = candidate.get("doi")
        if doi:
            haystacks.append(str(doi))
        primary_location = candidate.get("primary_location") or {}
        haystacks.append(str(primary_location.get("landing_page_url", "")))
        for location in candidate.get("locations", []):
            haystacks.append(str(location.get("landing_page_url", "")))
        joined = " ".join(haystacks)
        if arxiv_id in joined:
            score += 0.35

    return score


def format_citations(count: int) -> str:
    if count <= 0:
        return "New entry"
    if count == 1:
        return "1 citation"
    return f"{count} citations"


def parse_citation_count(text: str | None) -> int:
    if not text:
        return 0
    match = re.search(r"(\d+)", text)
    return int(match.group(1)) if match else 0


def refresh_publication(publication: dict[str, Any]) -> bool:
    candidates = collect_candidates(publication["title"], publication.get("year"))
    if not candidates:
        return False

    best = max(candidates, key=lambda item: candidate_score(publication, item))
    best_score = candidate_score(publication, best)
    if best_score < MIN_MATCH_SCORE:
        return False

    cited_by_count = int(best.get("cited_by_count") or 0)
    new_value = format_citations(cited_by_count)
    if publication.get("citations") == new_value:
        return False

    publication["citations"] = new_value
    return True


def main() -> None:
    publications = load_yaml(PUBLICATIONS_PATH)
    profile = load_yaml(PROFILE_PATH)

    changed = 0
    for publication in publications:
        if refresh_publication(publication):
            changed += 1

    total_citations = sum(parse_citation_count(pub.get("citations")) for pub in publications)
    profile["citations"] = format_citations(total_citations)

    dump_yaml(PUBLICATIONS_PATH, publications)
    dump_yaml(PROFILE_PATH, profile)

    print(f"Updated citations for {changed} publication(s); profile total is now {total_citations}.")


if __name__ == "__main__":
    main()
