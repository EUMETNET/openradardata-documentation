# 1. Overview

The **Open Radar Data (ORD) API** is a service, which provides access to EUMETNET OPERA weather radar data and products and to links of a selection of national weather radar products. 

**ORD API** was developed within the EU- and EUMETNET-funded [RODEO project](https://rodeo-project.eu/), which created a user interface and Application Programming Interfaces (APIs) for accessing meteorological datasets designated as High Value Datasets (HVDs) under the EU Implementing Regulation (EU) 2023/138 of the EU Open Data Directive (EU) 2019/1024. This project is also in line with WMO WIS 2.0 strategy. 

Weather radar data are also classified as HVDs and, accordingly, one of the aims of RODEO is to provide near real-time and archived weather radar observations. The radar data ispublished both via a message queue using [MQTT](https://mqtt.org/) and through [EDR](https://ogcapi.ogc.org/edr/)-compliant APIs. Metadata will also be made available via [OGC Records](https://ogcapi.ogc.org/records/) APIs. The ORD API can be reached via **MeteoGate** which is a ‘One-Stop Shop’ for meteorological and hydrological products and data (more information can be found in [MeteoGate](https://meteogate.eu/)).

The **ORD API** enables users to access radar data for visualization, analysis, and integration into other systems. For EUMETNET Members, the **Ingest API** focuses on data ingestion, allowing EUMETNET Members to provide local stored data (ODIM, GeoTIFF) references. The ORD API store the latest 24h radar data. The archive system will be implemented in later stage (TBD). 

The software [Open Radar Data API](https://radar.meteogate.eu/api/) and the related [Open Radar Data Ingest API](https://radar.meteogate.eu/ingest/) are located at [European Weather Cloud](https://europeanweather.cloud/). The EUMETNET OPERA datasets in 24-cache are available at the S3 Bucket [openradar-24h](https://s3.waw3-1.cloudferro.com/openradar-24h/). The **ORD API** is also available from [meteogate.eu](https://api.meteogate.eu/ord/edr).

---

## Published datasets in ORD API
There are three types of data available via ORD.
### 1. European single-site volume radar data
**European single-site volume weather radar** data are available through the EUMETNET OPERA programme, both as a 24-hour rolling cache and as an extensive archive (TBD). The data supply is forwarded directly from the incoming OPERA radar volume data as they are collected from the EUMETNET radar data providers and released with the authorisation of each provider. The data generally include:
  * unfiltered reflectivity factor (TH)
  * Doppler-filtered and cleaned reflectivity factor, known as the “best possible” reflectivity (DBZH)
  * radial velocity data (VRADH)

Currently, EUMETNET OPERA does not exchange dual-polarisation data. These are planned for inclusion in the coming years within the OPERA data exchange, after which they will also be supplied through the ORD API.

The data are provided in **ODIM BUFR** format for older datasets and in **ODIM HDF5** format for more recent ones. Some encoders or links to encoders are planned (TBD), for example [xradar](https://github.com/openradar/xradar). **[ODIM](https://eumetnet.eu/wp-content/uploads/2021/07/ODIM_H5_v2.4.pdf)** data model versions 2.0 to 2.4 have been used, noting that these versions are not always backward compatible.

It should be noted that scanning strategies, data-processing chains (including thresholds and algorithms), definitions of scan time, spatial and temporal resolution, and file structures vary between OPERA Members, resulting in heterogeneous datasets. Dealiasing of VRADH is not performed consistently at the national level, and is currently not applied centrally within OPERA. Data may be transmitted either as full volumes or on a scan-by-scan basis, with radar variables either combined in a single file or distributed across multiple files.

### 2. EUMETNET OPERA composite products
**OPERA composite products (provided by OPERA production called ODYSSEY, CIRRUS, and NIMBUS)** are available both as a 24-hour rolling cache and as a long-term archive dating back to 2012 (TBD). These products are provided by the EUMETNET OPERA programme in ODIM HDF5 and cloud-optimized GeoTIFF formats (TBD).  The composite products are based on incoming polar scans and volumes of filtered reflectivity. The composites cover the whole of Europe (area: 3,800 × 4,400 km2) in a Lambert Equal Area projection with approx. corner coordinates: (70 N 30 W), (70N 50E), (32N 15W), and (32 N 30E). 

There are three products on offer from the OPERA suite of products:

**OPERA Instantaneous Maximum Reflectivity (in dBZ)** 
 * In the maximum reflectivity composite each composite pixel contains the maximum of all polar cell values of the contributing radars at that location.
 * ODYSSEY production 2012-10/2024 and CIRRUS production 07/2024 –
 * In ODYSSEY production covering years of 01/2011- 10/2024, the composites are all updated every 15 minutes and issued ca. 15 minutes after data time with 2 x 2 km    resolution. The example image of ODYSSEY maximum reflectivity composite is shown in Figure 1. In the new production (07/2024 -) the CIRRUS products are with higher spatial resolution of 1 x 1 km and update cycle of 5 minutes.

**OPERA Instantaneous Surface Rain rate composite (in mm/h)** 
 * ODYSSEY production 2012-10/2024 and NIMBUS production 07/2024 -
 * In the ODYSSEY rain rate composite, each composite pixel is a weighted average of the valid pixels of the contributing radars, weighted by a quality index, the distance from center of the pixel and an exponential index related to inverse of the beam altitude. Whereas in NIMBUS production the compositing algorithm is based on the lowest elevation angle only.
 * Measured reflectivity values are converted to rainfall (mm/h) using the Marshall-Palmer equation.

**OPERA One Hour rainfall Accumulation (in mm)** 
 * Rainfall accumulation is the sum of the previous four 15-minute rain-rate products.
 * ODYSSEY production 2012-10/2024 and NIMBUS production 07/2024 -

Four quality filters are applied to the OPERA incoming volume data prior to compositing (Saltikoff et al. 2019). The data sharing model used in OPERA is an in-house developed ODIM (OPERA Data Information Model) both in BUFR and HDF5 for older production, solely HDF5 for the new production. The current ODIM specifications can be found from EUMETNET OPERA weather radar information model for implementation with the HDF5 file format Version 2.41 (ODIM 2.41). 


### 3. National radar products
National radar products, e.g. national radar composites, rain rate composites, accumulation products, and echo tops. These are provided as a link to be downloaded from the national interfaces, and typically in ODIM HDF5 or cloud-optimized GeoTiffs (TBD).



### OPERA Composites Data (ODYSSEY, CIRRUS, NIMBUS)
The composites cover the whole of Europe (area: 3,800 × 4,400 km2) in a Lambert Equal Area projection with approx. corner coordinates: (70 N 30 W), (70N 50E), (32N 15W), and (32 N 30E). In ODYSSEY production covering years of 01/2011- 10/2024, the composites are all updated every 15 minutes and issued ca. 15 minutes after data time with 2 x 2 km resolution. The example image of ODYSSEY maximum reflectivity composite is shown in Figure 1. In the new production (07/2024 -) the CIRRUS products are with higher spatial resolution of 1 x 1 km and update cycle of 5 minutes. The composite products are based on incoming polar scans and volumes of filtered reflectivity.

There are three products on offer from the OPERA suite of products:

**OPERA Instantaneous Maximum Reflectivity (in dBZ)** 
•	In the maximum reflectivity composite each composite pixel contains the maximum of all polar cell values of the contributing radars at that location.
•	ODYSSEY production 2012-10/2024 and CIRRUS production 07/2024 –

**OPERA Instantaneous Surface Rain rate composite (in mm/h)** 
•	ODYSSEY production 2012-10/2024 and NIMBUS production 07/2024 -
•	In the ODYSSEY rain rate composite, each composite pixel is a weighted average of the valid pixels of the contributing radars, weighted by a quality index, the distance from center of the pixel and an exponential index related to inverse of the beam altitude. Whereas in NIMBUS production the compositing algorithm is based on the lowest elevation angle only.
•	Measured reflectivity values are converted to rainfall (mm/h) using the Marshall-Palmer equation.

**OPERA One Hour rainfall Accumulation (in mm)** 
•	Rainfall accumulation is the sum of the previous four 15-minute rain-rate products.
•	ODYSSEY production 2012-10/2024 and NIMBUS production 07/2024 -

Four quality filters are applied to the OPERA incoming volume data prior to compositing (Saltikoff et al. 2019). The data sharing model used in OPERA is an in-house developed ODIM (OPERA Data Information Model) both in BUFR and HDF5 for older production, solely HDF5 for the new production. The current ODIM specifications can be found from EUMETNET OPERA weather radar information model for implementation with the HDF5 file format Version 2.41 (ODIM 2.41). 

### OPERA Database
OPERA Database is manually maintained table by the OPERA radar data providers and by the Croatian Meteorological and Hydrological Service (DHMZ). It is sporadically updated, at least twice a year. The available formats are json, xlsx and csv and it can be automatically pushed to ORD API. 

### National volume radar data 
Via the ORD API, the plan is to supply the incoming OPERA radar volume data as it is collected from the EUMETNET radar data providers. Typically, the number of incoming OPERA files is around 340,000 per day, amounting to approximately 45 GB daily. The data generally includes unfiltered reflectivity factor (TH), Doppler-filtered and cleaned reflectivity factor, known as "best possible" reflectivity (DBZH), and radial velocity data (VRADH). 

However, the scanning strategies, data processing chains with chosen thresholds and algorithms, definitions of scanning time, spatial and temporal resolution of data, and file structures vary nationally, resulting in heterogeneous datasets. The dealiasing of VRADH is not consistently performed nationally, and currently, it is also not applied centrally in OPERA. Data can be sent as volumes or on a scan-by-scan basis, with radar variables either combined in the same file or separated into different files. 

The OPERA volume data archive dates to 2011, but the data exhibits significant variability over the years. The older datasets can be quite different from the newer ones. The ODIM standard has been followed since the inception of OPERA volume data exchange; older datasets are usually in BUFR format, while newer ones are in HDF5. ODIM data format model versions 2.0 to 2.4 have been applied, but these are not always backward compatible. Due to computational resource constraints, the plan for ORD supply does not include converting the older radar datasets to HDF5 or newer versions of ODIM; this conversion is left to the users. Some encoders or links to encoders are planned to be provided.

Not all countries are part of the EU and are therefore not bound by the HVD regulation. As a result, not all OPERA members share their data via the ORD API. Additionally, some EU member states have chosen not to use the ORD API, opting instead to develop their own interfaces, while others use both the ORD API and their national solutions. Currently, six NMSs have declined to supply their data via the ORD API.


### National composites or products 
During the design phase, the WP6 working group proposed incorporating a demonstration of national products into the API development to support National Meteorological Services (NMSs) in complying with the HVD Implementation Act requirements. These products are handled differently in both back-end processing and data supply of ORD API compared to OPERA datasets, composites, and radar volumes.

The demonstration of national products includes only specific product types, such as reflectivity, rain rate, and accumulation composites, vertical wind profiles, and echo tops. The datasets are provided in either HDF5 ODIM or Cloud-optimized GeoTIFF (CoG) formats and are archived and supplied through national interfaces. Within the ORD API, only a data discovery function and a link to access the data are provided. This requires radar product providers to supply metadata in JSON format to the ORD API to ensure proper data cataloging and accessibility.

Currently shared national products are:

**FMI precipitation accumulation composites of 1h, 3h, 6h, and 24 h (in mm) in CoG format**
•	FMI has an open data policy where the data and products are stored in AWS (Amazon Web Services) S3 buckets 
•	The JSON files ingested to ORD API include the link to AWS S3 location 

**KNMI 2D- and 3D -reflectivity composites in HDF5 format** 
•	KNMI has an open data policy where the data and products are stored in AWS S3 buckets but with the dedicated API key  

**Met Norway national reflectivity composites in in CoG format**
•	MET Norway has an open data policy where radar data is stored in an open API using a local OGC Stac implementation for sharing the datafiles. Data is produced in CoG format to demonstrate the use of GeoWeb as a map tool for showing the data. The functionality of MeteoGate running on GeoWeb has not yet been finalized.
•	The JSON files ingested to ORD API include the link to the STAC API


## 1.2 Data Policy
In OPERA, volume radar data remains the property of the radar data provider. Therefore, the provider has the authority to define the conditions under which the data can be distributed from OPERA or whether it is restricted for the exclusive use of EUMETNET Members. Before radar data is ingested into the EWC and stored in S3 buckets, any data without the necessary authorization is excluded and not archived in EWC.

A survey was conducted to assess the rights to share data via the ORD API and determine the applicable licensing terms. Most OPERA Members have agreed to share their data, with most opting for the CC BY 4.0 license. 




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
---


The property rights of OPERA composite products are held by EUMETNET, which has decided to distribute these products under the CC BY 4.0 license.

Each NMS independently defines the property rights and licensing terms for its radar data. This information is communicated through MQTT messages. All data are accompanied by the appropriate license information, accessible via the ORD API or MQTT streams. License details are automatically included either in the files and metadata ingested into the system or via an authorization table managed by OPERA.



