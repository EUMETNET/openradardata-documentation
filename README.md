# Open Radar Data (ORD) API Documentation

This repository contains the documentation for the **Open Radar Data (ORD) API** service.

The ORD API service provides access to EUMETNET OPERA composite products, volume radar data, and a portal for retrieving a selection of national radar products for demonstration.

## Branches in this Repository

- `docs-dev` — Development branch for editing and writing documentation (Markdown).
- `main` — Integration branch for reviewed and accepted changes.
- `gh-pages` — Static html pages built automatically from main using MKDoc and published via GitHub Pages.

## Published Documentation Site

https://api.meteogate.eu/documentation/eu-eumetnet-weather-radar (TBD)

---

## Want to contribute to ORD documentation?

Documentation is written, updated and reviewed in [`docs-dev`](https://github.com/eumetnet/openradardata-documentation/tree/docs-dev) branch.  All documentation work should be done in this branch before publishing.

> Changes from this branch are reviewed and merged into the `main` branch by a pull request. The documentation is then built and published from `main` to the `gh-pages` branch via MkDocs and GitHub Actions.

## How to Contribute

1. **Clone the repository** and switch to the `docs-dev` branch:
   ```bash
   git clone https://github.com/<org-or-user>/<repo>.git
   cd <repo>
   git checkout docs-dev
   ```

2. **Edit or create Markdown files** in the `docs/` directory.

3. **Preview the documentation locally** using MkDocs:
   ```bash
   mkdocs serve
   ```
   Then open `http://127.0.0.1:8000` in your browser.

4. **Commit and push your changes**:
   ```bash
   git add .
   git commit -m "Describe your update"
   git push origin docs-dev
   ```

5. **Open a pull request from `docs-dev` to `main`**  
   This allows review before the changes are published.

6. **Once merged into `main`, the site is built and deployed** to the `gh-pages` branch.  
   The site is automatically built and deployed using a GitHub Actions workflow. 
   The MkDocs tool is used to generate static HTML pages from the Markdown files, and GitHub Pages hosts the final published site.
   No manual building or deployment is required — changes are automatically published once merged.

---

## Documentation Structure

All documentation source files are located in the `docs/` directory, organized by section:

- `1-ORD-API-overview.md` – Homepage
- `2-ORD-API-discovering-and-accessing-data.md`, `3-ORD-API-publishing-data.md`, etc. – Section content
- `glossary.md` – Supporting material

---

## Tools

- **MkDocs** – Static site generator for documentation
- **Material for MkDocs** – Theme used for styling and navigation
- **GitHub Pages** – Used for publishing the site from the `gh-pages` branch
- **Read the Docs** *(optional)* – Alternative platform for documentation hosting

---

## Need Help?

For questions, feedback, and conversations, you are welcome to join the [MeteoGate Community Discussion Group](https://github.com/orgs/Meteogate/discussions).

---

## License

All documentation in this repository is © 2025 EUMETNET and licensed under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
   

## Contacts
support.opera@eumetnet.eu
