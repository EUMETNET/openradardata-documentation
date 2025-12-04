# Open Radar Data (ORD) API Documentation

This repository contains the documentation for the **Open Radar Data (ORD) API** service.

The ORD API service provides access to EUMETNET OPERA composite products, volume radar data for operational use, archived volume data for research purposes, and a portal for retrieving a selection of national radar products for demonstration.

## Branches in this Repository

- `docs-dev` — Development branch for editing and writing documentation (Markdown).
- `main` — Integration branch for reviewed and accepted changes.
- `gh-pages` — Static html pages built automatically from main using MKDoc and published via GitHub Pages.

## Published Documentation Site

https://api.meteogate.eu/documentation/eu-eumetnet-weather-radar

---

## RODEO

The [RODEO project](https://rodeo-project.eu/) develops a user interface and Application Programming Interfaces (API) for accessing meteorological datasets declared as High Value Datasets (HVD) by the EU Implementing Regulation (EU) 2023/138 under the EU Open Data Directive (EU) 2019/1024. The project also fosters the engagement between data providers and data users for enhancing the understanding of technical solutions being available for sharing and accessing the HVD datasets.
This project provides a sustainable and standardized system for sharing real-time weather observations and warnings in line with the HVD regulation and WMO WIS 2.0 strategy. These datasets are made available through open web services, so that they can be accessed by anyone.

# Open Radar Data (ORD)

The weather radar data is also considered as HVDs, and therefore, one of the goals of RODEO is to supply near real-time weather radar observations. The radar data will be published on both a message queue using [MQTT](https://mqtt.org/) and [EDR](https://ogcapi.ogc.org/edr/) compliant APIs. Metadata will also be made available through [OGC Records](https://ogcapi.ogc.org/records/) APIs. The system architecture is portable, scalable and modular for taking into account possible future extensions to existing networks and datasets. Diagrams of the system could be found here as [C4 diagrams](https://github.com/EUMETNET/openradardata-technical-architecture/tree/ingest/source/images/c4-container-openradar-wp6-user.png).


The **Open Radar API** enables users to access radar data for visualization, analysis, and integration into other systems. For EUMETNET Members, the **Ingest API** focuses on data ingestion, allowing EUMETNET Members to provide local stored data (**ODIM**, **GeoTIFF**) references. The API stored the latest 24h radar data. The archive system will be implemented in later stage (TBD). 
The software [Open Radar Data API](https://radar.meteogate.eu/api/) and the related [Open Radar Data Ingest API](https://radar.meteogate.eu/ingest/) are located at [European Weather Cloud](https://europeanweather.cloud/). The OPERA datasets in 24-cache are available at the S3 Bucket [openradar-24h](https://s3.waw3-1.cloudferro.com/openradar-24h/). The ORD API is also available from [meteogate.eu](https://api.meteogate.eu/ord/edr)



## Published datasets in ORD
There are three types of data available via ORD.
1. **European single-site volume radar data** are available through the EUMETNET OPERA programme, both as a 24-hour rolling cache and as an extensive archive (TBD). The data are provided in BUFR format for older datasets and in ODIM HDF5 format for more recent ones.
2. **European composite products** — including maximum reflectivity factor, instantaneous rain rate, and 1-hour rainfall accumulation — are available both as a 24-hour rolling cache and as a long-term archive dating back to 2012 (TBD). These products are provided by the EUMETNET OPERA programme in ODIM HDF5 and cloud-optimized GeoTIFF formats (TBD).
3. **National radar products**, e.g. national radar composites, rain rate composites, accumulation products, and echo tops. These are provided as a link to be downloaded from the national interfaces, and typically in ODIM HDF5 or cloud-optimized GeoTiffs (TBD).

---
## Getting Started

1. [ORD API User Instructions](ORD_API.md)
2. [Subscribe to notification messages](ORD_MQTT.md)
3. For EUMETNET Members only: [ORD Ingest API User Instructions](ORD_INGEST.md)
4. Visit the Swagger UI for the **Open Radar API** ([here](https://radar.meteogate.eu/api/docs)) and the **Ingest API** ([here](https://radar.meteogate.eu/ingest/docs)) to explore the endpoints and capabilities.
5. Public Meteogate API available via [meteo gateway](https://api.meteogate.eu/ord/edr)
6. [ORD S3 24h cache](https://s3.waw3-1.cloudferro.com/openradar-24h/)
7. [ORD S3 Archive](https://s3.waw3-1.cloudferro.com/openradar-archive/) TBD


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

- `index.md` – Homepage
- `1-overview.md`, `2-discovering-and-accessing-data.md`, etc. – Section content
- `glossary.md`, `references.md` – Supporting material

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
