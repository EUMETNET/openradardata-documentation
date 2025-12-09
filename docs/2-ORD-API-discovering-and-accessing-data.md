## Data Retrieval with Open Radar Data (ORD) API

### [Data available in ORD API](https://github.com/EUMETNET/openradardata-documentation/blob/main/docs/1-ORD-API-overview.md#published-datasets-in-ord-api)

**1. EUMETNET OPERA single-site radar data**
   * 24-hour rolling cache, with a long-term archive (2012–, TBD)
   * Formats: BUFR (older) and ODIM HDF5 (recent)
   * License: CC BY 4.0 (with exceptions noted in metadata)
   * Currently mainly includes:
        - DBZH (Doppler-filtered horizontal reflectivity factor, with national QC applied)
        - TH (unfiltered horizontal reflectivity factor)
        - VRADH (horizontal radial velocity)
        - Basic dual-pol variables (e.g. correlation coefficient, differential reflectivity, differential phase shift,                 specific differential phase) are planned to be added from 2027 onwards (TBD)

**2. European OPERA composite products**
  * Products: maximum reflectivity, instantaneous rain rate, 1-hour accumulation
  * TBDcoming later)
  * Formats: ODIM HDF5 and cloud-optimized GeoTIFF (TBD)
  * License: CC BY 4.0
     
**3. National radar products**
  * Examples of national composites, rain rate composites, accumulations, echo tops
  * Access: via links to national interfaces (24h access of links)
  * Formats: ODIM HDF5 or cloud-optimized GeoTIFF

---

### ORD API Examples

The **Open Radar Data API** is ideal for retrieving and integrating radar data into various workflows. Here are some examples:

**1. EUMETNET OPERA single-site volume radar data:**
   - Retrieve single site (Hurum, Norway) radar intensity data (DBZH) in ODIM format for specific time range (2025-10-13T12:10Z/2025-10-13T12:40Z) and elevations lower than 5&deg;:
        1. Open [ORD API Swagger UI](https://radar.meteogate.eu/api/docs) and select: collections/observations/localtions/{location_id}
        2. Click to "Try it out" button and set the query parameters:
        3. ``location_id``: 0-20000-0-01498
        4. ``parameter-name``: leave blank, set it below separately(standard_name:level:*:*)
        5. ``datetime``: 2025-10-13T12:10Z/2025-10-13T12:40Z
        6. ``standard_name``: DBZH
        7. ``level``: ../5.0
        8. ``format``: ODIM
        9. ``method``: scan 
        10. ``duration`` is blank

            ![ORD Query Parameters](/Images/ORD_API_location.png)

        11. Click the Execution button and the response available. See the ``curl`` example the request url and the response below

            ![ORD Response](docs/Images/ORD_API_location_response.png)

        12. Direct meteogate query link:
        ```
        https://api.meteogate.eu/ord/edr/collections/observations/locations/0-20000-0-01498?datetime=2025-10-13T12%3A10Z%2F2025-10-13T12%3A40Z&f=CoverageJSON&level=..%2F5.0&format=ODIM
        ```
        Note: Update the datetime field within this URL.

        12. ODIM data are downloadable from these links:
            ![ORD Response](source/images/ORD_API_location_response_links.png)

        13. Using [aws](https://aws.amazon.com/cli/) tool

            Check the file existing in the S3 bucket:
            ```bash
            aws s3 ls s3://openradar-24h/2025/10/13/NO/nohur/PVOL/   --endpoint-url https://s3.waw3-1.cloudferro.com/  --no-sign-request
            ```
            Check the daily OPERA data in the S3 bucket:
            ```bash
            aws s3 ls s3://openradar-24h/2025/10/16/OPERA/COMP/   --endpoint-url https://s3.waw3-1.cloudferro.com/  --no-sign-request
            ```
            Copy file to new_local_filename.h5:
            ```bash
            aws s3  cp s3://openradar-24h/2025/10/16/OPERA/COMP/OPERA@20251016T0220@0@DBZH.h5 ./new_local_filename.h5  --endpoint-url https://s3.waw3-1.cloudferro.com/  --no-sign-request
            ```
        

        14. radar_meta(ODIM attributes) section is below the links:
            ```json
                "metocean:wigosId": "0-20000-0-01498",
                "metocean:platform_name": "[nohur]",
                "metocean:format": "ODIM",
                "metocean:radar_meta": {
                    "object": "PVOL",
                    "elangle": 1,
                    "nbins": 960,
                    "rstart": 0,
                    "rscale": 250,
                    "nrays": 360,
                    "a1gate": 338,
                    "product": "SCAN",
                    "beamwH": 0.95
                }
            ```
        15. If no data for the specified query the response is 204.

            ![ORD Response](source/images/ORD_API_response_no_content.png)

        

   - Query Radial velocity volumes:
        1. ``standard_name``: VRADH

   - Retrieve all Dutch data.
        1. ``location_id``: 0-20010-\*-nl\*

2. **OPERA composite products:**
   - Fetch composite product from OPERA production
        1. ``standard_name``: RATE or ACRR or DBZH

   - OPERA products:
        1. ``location_id``: 0-\*-\*-OPERA

   - Query ODIM format:
        1. ``format``: ODIM

   - Composite:
        1. ``method``: comp

4. **Select observation items:**
   - Retrieve German sites from boundary box area (-5.5,18.0,72.0,82.1) where raw radar reflectivity data (TH) is available in ODIM format for specific time range (2025-10-13T12:10Z/2025-10-13T12:40Z):
        1. Open [ORD API](https://radar.meteogate.eu/api/docs) and select: collections/observations/items
        2. Click to "Try it out" button and set the query parameters:
        3. ``bbox``: -5.5,18.0,72.0,82.1
        4. ``datetime``: 2025-10-13T12:10Z/2025-10-13T12:40Z
        5. ``id``: leave blank
        6. ``parameter-name``: leave blank, set it below separately (standard_name:level:*:*)
        7. ``naming_authority``: de.dwd
        8. ``institution``, ``platform``: leave blank
        9. ``standard_name``: TH
        10. ``unit``, ``instrument``, ``level``: leave blank
        11. ``format``: ODIM,
        12. ``method``: scan
        13. ``period``, ``f``: leave blank
        Result 
        ```json
            {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "geometry": {
                    "type": "scan",
                    "coordinates": [
                    9.694533,
                    52.460083
                    ]
                },
                "properties": {
                    "summary": "Radar data from OPERA network.",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "naming_authority": "de.dwd",
                    "platform": "0-20000-0-10339",
                    "platform_name": "[dehnr]",
                    "standard_name": "TH",
                    "unit": "%",
                    "level": 0.5,
                    "period": "PT30S",
                    "parameter_name": "TH:0.5:point:PT30S",
                    "timeseries_id": "07ea52bf21af5399cbc165982559d2ea",
                    "radar_meta": {
                    "object": "SCAN",
                    "elangle": 0.4998779296875,
                    "nbins": 720,
                    "rstart": 0,
                    "rscale": 250,
                    "nrays": 360,
                    "a1gate": 100,
                    "product": "SCAN",
                    "frequency": 5641692508.103789,
                    "beamwH": 0.9,
                    "beamwV": 0.9
                    },
                    "format": "ODIM",
                    "platform_vocabulary": "https://oscar.wmo.int/surface/rest/api/search/station?wigosId=0-20000-0-10339",
                    "method": "scan",
                    "data": "https://radar.meteogate.eu/api/collectionscollections/observations/locations/0-20000-0-10339?=parameter-name=TH:0.5:point:PT30S"
                },
                "id": "07ea52bf21af5399cbc165982559d2ea"
                },
                {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                    6.967111,
                    51.405649
                    ]
                },
                "properties": {
                    "summary": "Radar data from OPERA network.",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "naming_authority": "de.dwd",
                    "platform": "0-20000-0-10410",
                    "platform_name": "[deess]",
                    "standard_name": "TH",
                    "unit": "%",
                    "level": 0.5,
                    "period": "PT30S",
                    "parameter_name": "TH:0.5:point:PT30S",
                    "timeseries_id": "126aad398d3e52c3151a5cc5f7a0ffb2",
                    "radar_meta": {
                    "object": "SCAN",
                    "elangle": 0.4998779296875,
                    "nbins": 720,
                    "rstart": 0,
                    "rscale": 250,
                    "nrays": 360,
                    "a1gate": 100,
                    "product": "SCAN",
                    "frequency": 5606682004.950664,
                    "beamwH": 0.9,
                    "beamwV": 0.9
                    },
                    "format": "ODIM",
                    "platform_vocabulary": "https://oscar.wmo.int/surface/rest/api/search/station?wigosId=0-20000-0-10410",
                    "method": "point",
                    "data": "https://radar.meteogate.eu/api/collectionscollections/observations/locations/0-20000-0-10410?=parameter-name=TH:0.5:point:PT30S"
                },
                "id": "126aad398d3e52c3151a5cc5f7a0ffb2"
                },...
            ]...
            }

        ```
        

