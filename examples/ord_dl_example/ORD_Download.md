# Open Radar Data Download Example

This script connects to the MQTT_BROKER and subscribes to the TOPIC. Then is downloads ODIM files from S3 bucket.

## Installation
1. Create python virtual environment and activate

```bash
python3 -m /path_to/ord-venv
source /path_to/ord-venv/bin/activate
```

2. Install requirements
```bash
pip install --upgrade pip
pip install  -r ./requirements.txt
```

3. Set environment variables(optional)

| Name                | Description                        | Default value         |
|---------------------|------------------------------------|-----------------------|
| ODIM_DL_DIR         | Download directory for ODIM files  | ./odim_files          |
| MQTT_BROKER         | MQTT Broker address                | radar.meteogate.eu    |
| MQTT_PORT           | MQTT Port                          | 1883                  |
| S3_BUCKET_NAME      | S3 bucker name                     | openradar-24h         |
| S3_ENDPOINT_URL     | S3 endpoint url                    | https://s3.waw3-1.cloudferro.com/ |
| TOPIC               | Topic to subscribe                 | #                     |


## Usage
```bash
[ord-venv] python3 ord_dl_example.py
```

