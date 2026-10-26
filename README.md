# Zhizhen Zhang — Academic Homepage

A responsive Jekyll site for https://daisy-zzz.github.io/homepage/.

The layout takes inspiration from the UQMM academic website: white background,
a narrow reading column, compact top navigation, and clearly separated content
sections. Forest green (#174b3c) is used for links, headings, and venue labels.
The CSS is original and uses system fonts; no external framework or font service
is required. The portrait retains its original colors.

## Maintain content

- `_data/profile.yml`: biography, research interests, supervisors, contact links.
- `_data/publications.yml`: papers, newest first. `homepage_selected: true` adds a
  paper to the homepage. `paper_url`, `project_url`, and `code_url` enable links.
- `_data/highlights.yml`: news.
- `_data/main_sections.yml`: service, teaching, awards, academic activities.
- `_data/navigation.yml`: navigation links.
- `_includes/publication.html`: shared publication layout for both pages.
- `assets/css/main.css`: forest-green theme, responsive layout, print styles.
- `assets/js/main.js`: accessible mobile navigation and publication search.

All papers remain visible and navigation remains usable without JavaScript.
Missing method figures use the labeled preview placeholder. Citation counts are
not displayed; Google Scholar is linked for current counts.

## Publication assets

PolicyWeave uses its project page's original method diagram. PPCL and HierCas use
original paper figures. MobiGuide now links to arXiv:2604.01567v2 and uses its
Figure 4 method overview, resized for web display. Source URLs are retained in
the publication data. MobiGuide is labeled as an arXiv preprint.

## Preview and deployment

Run `bundle install` followed by `bundle exec jekyll serve`; open
http://127.0.0.1:4000/homepage/.

The existing `.github/workflows/pages.yml` builds and deploys on pushes to `main`.
Keep `_config.yml`'s `url` and `baseurl` unchanged.
