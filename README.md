# Open Radar API Documentation


## RODEO

The [RODEO project](https://rodeo-project.eu/) develops a user interface and Application Programming Interfaces (API) for accessing meteorological datasets declared as High Value Datasets (HVD) by the EU Implementing Regulation (EU) 2023/138 under the EU Open Data Directive (EU) 2019/1024. The project also fosters the engagement between data providers and data users for enhancing the understanding of technical solutions being available for sharing and accessing the HVD datasets.
This project provides a sustainable and standardized system for sharing real-time weather observations and warnings in line with the HVD regulation and WMO WIS 2.0 strategy. These datasets are made available through open web services, so that they can be accessed by anyone.

# Open Radar Data (ORD)

The weather radar data is also considered as HVDs, and therefore, one of the goals of RODEO is to supply near real-time weather radar observations. The radar data will be published on both a message queue using [MQTT](https://mqtt.org/) and [EDR](https://ogcapi.ogc.org/edr/) compliant APIs. Metadata will also be made available through [OGC Records](https://ogcapi.ogc.org/records/) APIs. The system architecture is portable, scalable and modular for taking into account possible future extensions to existing networks and datasets. Diagrams of the system could be found here as [C4 diagrams](https://github.com/EUMETNET/openradardata-technical-architecture/tree/ingest/source/images/c4-container-openradar-wp6-user.png).


The **Open Radar API** enables users to access radar data for visualization, analysis, and integration into other systems. For EUMETNET Members, the **Ingest API** focuses on data ingestion, allowing EUMETNET Members to provide local stored data (**ODIM**, **GeoTIFF**) references. The API stored the latest 24h radar data. The archive system will be implemented in later stage (TBD). 
The software [Open Radar Data API](https://radar.meteogate.eu/api/) and the related [Open Radar Data Ingest API](https://radar.meteogate.eu/ingest/) are located at [European Weather Cloud](https://europeanweather.cloud/). The OPERA datasets in 24-cache are available at the S3 Bucket [openradar-24h](https://s3.waw3-1.cloudferro.com/openradar-24h/). The ORD API is also available from [meteogate.eu](https://api.meteogate.eu/ord/edr)



## Published datasets in ORD
There are three types of data available via ORD.
1. European single-site radar data are available through the EUMETNET OPERA programme, both as a 24-hour rolling cache and as an extensive archive (TBD). The data are provided in BUFR format for older datasets and in ODIM HDF5 format for more recent ones.
2. European composite products — including maximum reflectivity factor, instantaneous rain rate, and 1-hour rainfall accumulation — are available both as a 24-hour rolling cache and as a long-term archive dating back to 2012 (TBD). These products are provided by the EUMETNET OPERA programme in ODIM HDF5 and cloud-optimized GeoTIFF formats (TBD).
3. National radar product, e.g. national radar composites, rain rate composites, accumulation products, and echo tops. These are provided as a link to be downloaded from the national interfaces, and typically in ODIM HDF5 or cloud-optimized GeoTiffs (TBD).

---
## Getting Started

1. [ORD API User Instructions](ORD_API.md)
2. [Subscribe to notification messages](ORD_MQTT.md)
3. For EUMETNET Members only: [ORD Ingest API User Instructions](ORD_INGEST.md)
4. Visit the Swagger UI for the **Open Radar API** ([here](https://radar.meteogate.eu/api/docs)) and the **Ingest API** ([here](https://radar.meteogate.eu/ingest/docs)) to explore the endpoints and capabilities.
5. Public Meteogate API available via [meteo gateway](https://api.meteogate.eu/ord/edr)
6. [ORD S3 24h cache](https://s3.waw3-1.cloudferro.com/openradar-24h/)
7. [ORD S3 Archive](https://s3.waw3-1.cloudferro.com/openradar-archive/) TBD
   

## Contacts
support.opera@eumetnet.eu
