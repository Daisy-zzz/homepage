# Academic Homepage

GitHub Pages friendly academic homepage for Zhizhen Zhang under `/home/uqzzha39/Projects/academic-homepage`.

## Structure

- `_config.yml`: Jekyll site settings for GitHub Pages
- `_layouts/default.html`: shared page layout
- `_data/profile.yml`: profile metadata
- `_data/publications.yml`: selected publications
- `_pages/`: bio, publications, and links pages
- `assets/css/main.css`: custom academic visual theme
- `index.html`: homepage using Liquid and Jekyll front matter

## Make It Public On GitHub Pages

1. Create a public GitHub repository.
2. If you want the site at `https://YOUR_GITHUB_USERNAME.github.io`, name the repository `YOUR_GITHUB_USERNAME.github.io`.
3. Push this folder to that repository.
4. Update `_config.yml`:
   - Set `url` to your real GitHub Pages URL.
   - Keep `baseurl` empty for a user site.
   - If you publish from a project repository instead, set `baseurl` to `"/REPOSITORY-NAME"`.
5. This repo already includes a GitHub Actions workflow at `.github/workflows/pages.yml`.
6. In GitHub, open `Settings` -> `Pages`.
7. Under `Build and deployment`, choose `GitHub Actions`.

GitHub Pages will build the Jekyll site and publish it publicly.

## Local Preview

This repo includes a `Gemfile` for standard GitHub Pages local preview workflows.

Typical local commands are:

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000`.

## Content Notes

- Publication metadata and profile details were assembled from the public Google Scholar page:
  `https://scholar.google.com/citations?user=X1sJkM8AAAAJ&hl=en`
- Contact details were cross-checked against the public UQ profile:
  `https://eecs.uq.edu.au/profile/12064/zhizhen-zhang`
- The bio and research descriptions are concise summaries inferred from those public sources.
