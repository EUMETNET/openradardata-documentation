#
# Open Radar Data Example
#
# istvans@met.no
#
# This script connects to the MQTT_BROKER and subscribes to the TOPIC
# Then is downloads ODIM files when
# the link is started by S3_ENDPOINT_URL + S3_BUCKET_NAME.


import boto3
import json
import os
import paho.mqtt.client as mqtt
from botocore import UNSIGNED
from botocore.client import Config

cnt_ok = 0
cnt_fail = 0

DL_DIR = os.getenv("ODIM_DL_DIR", "./odim_files")
os.makedirs(DL_DIR, exist_ok=True)

# ########################## ENV VALUES ####################################

MQTT_BROKER = os.getenv("MQTT_BROKER", "radar.meteogate.eu")
MQTT_PORT = int(os.getenv("MQTT_PORT", "8884"))

MQTT_USER = os.getenv("MQTT_USER", "everyone")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "everyone")
WEBSOCKET_PATH = os.getenv("WEBSOCKET_PATH", "/ordmqtt")

# Examples: eu.eumetnet no.met nl.knmi
# TOPIC = os.getenv("ORD_TOPIC","#")  # all
TOPIC = os.getenv("ORD_TOPIC", "ORD/eu.eumetnet/0-20010-0-OPERA/DBZH/#")  # OPERA DBZH composite
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "openradar-24h")
S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL", "https://s3.waw3-1.cloudferro.com/")

# ########################## S3 BUCKET #####################################

if S3_ENDPOINT_URL[-1] != "/":
    S3_ENDPOINT_URL += "/"
print(S3_ENDPOINT_URL)
s3_url = S3_ENDPOINT_URL + S3_BUCKET_NAME
s3_url_len = len(s3_url)

s3_client = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT_URL,
        config=Config(signature_version=UNSIGNED)
    )

prefix = ""
# Check S3 bucket
try:
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=prefix)

except Exception as e:
    print(f"Error listing objects: {e}")
    exit(1)


# ######################## MQTT BROKER ####################################

# Define the callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the broker!")
        # Subscribe to the desired topic
        client.subscribe(TOPIC)  # Replace with your topic
    else:
        print(f"Failed to connect, return code {rc}")


# Define the callback when a message is received on the subscribed topic
def on_message(client, userdata, msg):

    ord_msg = json.loads(msg.payload.decode())
    for link in ord_msg["links"]:
        if link["href"][:s3_url_len] == s3_url:
            # print("URL: {0}".format(link["href"]))
            dl_file = link["href"]
            delim = "/"
            last_delim = dl_file.rfind(delim)
            ingest_file = DL_DIR + "/" + dl_file[last_delim+1:]

            if os.path.exists(ingest_file):
                # print(f"File already downloaded, skip: {ingest_file}")
                break

            dl_key = dl_file[s3_url_len+1:]

            try:
                print("Downloading: {0}".format(dl_key), end="")
                s3_client.download_file(S3_BUCKET_NAME, dl_key, ingest_file)
                print("\tOK")

            except Exception as e:
                print(f"Error downloading file: {e}")

            break


# Create an MQTT client instance
client = mqtt.Client(transport="websockets")
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.tls_set()
client.tls_insecure_set(True)
client.ws_set_options(path=WEBSOCKET_PATH)

# Attach the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
broker = MQTT_BROKER
port = MQTT_PORT

client.connect(broker, port)

# Start the network loop to process incoming and outgoing messages
client.loop_forever()
