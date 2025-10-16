---
## Data Sharing with Ingest API

The ORD ingestion API includes three endpoints for sharing data:

### 1. BUFR Endpoint
- Used for uploading and sharing **BUFR files**.
- For **OPERA to ingest the European single site data** to European Weather Cloud S3 storage
- The ingester module:
  - Extracts metadata from BUFR files and stores it in the database.
  - Uploads the original (or renamed) BUFR file to the ORD S3 bucket.

### 2. ODIM Endpoint
- Processes **ODIM files**.
- For **OPERA to ingest the European single site data and OPERA composites** to European Weather Cloud S3 storage
- The ingester module:
  - Extracts metadata from ODIM files and stores it in the database.
  - Uploads the original (or renamed) ODIM file to the ORD S3 bucket.

### 3. JSON Endpoint
- Enables sharing **locally stored radar data**.
- For **National Meteorological Services (NMSs) to provide national products** via ORD
- Users provide radar metadata through the JSON endpoint.


**[Openradardata-validator](https://github.com/EUMETNET/openradardata-validator)** includes a JSON message generator for creating custom `json_upload_schema` files and a validator script to verify the schema. The message generator creates distinct JSON schemas for each quantity at each level.

---

### Ingest API Use Cases

The **Ingest API** is designed for uploading and processing radar data files. It supports the ingestion of **ODIM** and **BUFR** data formats as well as local file references via JSON.

Examples: TBD


