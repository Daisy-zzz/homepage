# Zhizhen Zhang — Academic Homepage

A lightweight, responsive Jekyll site for GitHub Pages at
https://daisy-zzz.github.io/homepage/.

The visual direction uses fog-white paper, ocean-blue ink, topographic contours,
a dotted connection route, and restrained signal-yellow accents. The terrain and
identity mark are original SVG assets. No build-time JavaScript framework, external
font service, analytics, or game assets are required.

## Maintain content

- `_data/profile.yml`: biography, supervisors, affiliation, and contact links.
- `_data/publications.yml`: publications in display order, newest years first.
  Set `homepage_selected: true` to feature a paper on the homepage. Set
  `venue_short` for the compact venue label; retain `venue` for the full citation.
  `paper_url`, `project_url`, and `code_url` independently enable their links.
  `teaser_image` is optional; missing figures are left blank and collapse on mobile.
- `_data/highlights.yml`: news, newest first.
- `_data/main_sections.yml`: reviewers, awards, teaching, and activities.
- `_data/navigation.yml`: primary navigation.
- `assets/css/main.css`: theme and mobile/print layouts.
- `assets/js/main.js`: progressively enhanced publication search. All papers
  remain visible when JavaScript is disabled.

The site links to Google Scholar for current citation counts; cached counts in the
data are not displayed. New publications should use verified author and venue
information, with workshops and preprints identified explicitly.

## Local preview

Requires Ruby and Bundler:

```bash
bundle install
bundle exec jekyll serve
```

Open http://127.0.0.1:4000/homepage/. The project base URL is `/homepage`.

## Deployment

The existing `.github/workflows/pages.yml` builds Jekyll and deploys GitHub Pages
on pushes to `main`. GitHub Settings → Pages should use GitHub Actions.
Keep the existing `url` and `baseurl` in `_config.yml` for this repository.

## September 2026 content update

- Added MobiGuide as an RSS 2026 OWN workshop publication.
- Removed AnchorVLA and SRHAC from the publication list at the owner's request.
- Added NeurIPS 2026 and ICLR 2027 reviewing; retained NeurIPS 2025 and CVPR 2026.
- Added original method figures for PPCL (Figure 2, page 4 of arXiv:2410.09345)
  and HierCas (Figure 1, page 4 of arXiv:2310.13219).
- Figure source URLs and figure/page numbers are stored with the publication data.
- MobiGuide and Resolving Spurious Temporal Location Dependency for Video Corpus
  Moment Retrieval retain their paper information with figures left blank, as approved
  by the site owner. These missing figures do not block publication.
