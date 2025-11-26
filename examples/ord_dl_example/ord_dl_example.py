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
import time
from botocore import UNSIGNED
from botocore.client import Config

cnt_ok = 0
cnt_fail = 0

# Check old files after dl_max downloads
# Don't delete old files: dl_max = 0
dl_max = 300
# Delete files older than dl_min minutes
dl_min = 2
dl_count = 0
dl_dir = os.getenv("ODIM_DL_DIR", "./odim_files")
os.makedirs(dl_dir, exist_ok=True)

# ########################## ENV VALUES ####################################

MQTT_BROKER = os.getenv("MQTT_BROKER", "radar.meteogate.eu")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

# Examples: eu.eumetnet no.met nl.knmi
TOPIC = os.getenv("ORD_TOPIC","#")  # all
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
    # for obj in response.get('Contents', []):
    #    print(f"Object Key: {obj['Key']}")

except Exception as e:
    print(f"Error listing objects: {e}")
    exit(1)


# ####################### DELETE OLD FILES #################################

def delete_old_files(directory, mins):
    del_cnt = 0
    cur_time = time.time()
    cutoff_time = cur_time - mins * 60

    print("Deleting files, at {0}".format(time.ctime(cur_time)))

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file's last modification time
            file_mtime = os.path.getmtime(file_path)

            # Check if the file is older than the cutoff time
            if file_mtime < cutoff_time:
                try:
                    # Delete the file
                    os.remove(file_path)
                    del_cnt += 1
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

    print(f"Deleted {del_cnt} files.")


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
    global dl_count
    global dl_max
    global dl_min
    global s3_client
    global cnt_ok
    global cnt_fail

    ord_msg = json.loads(msg.payload.decode())
    for link in ord_msg["links"]:
        if link["href"][:s3_url_len] == s3_url:
            # print("URL: {0}".format(link["href"]))
            dl_file = link["href"]
            delim = "/"
            last_delim = dl_file.rfind(delim)
            ingest_file = dl_dir + "/" + dl_file[last_delim+1:]

            if os.path.exists(ingest_file):
                # print(f"File already downloaded, skip: {ingest_file}")
                break

            dl_key = dl_file[s3_url_len+1:]

            try:
                print("Downloading: {0}".format(dl_key), end="")
                s3_client.download_file(S3_BUCKET_NAME, dl_key, ingest_file)
                print("\tOK")
                dl_count += 1

            except Exception as e:
                print(f"Error downloading file: {e}")

            if dl_max > 0 and dl_count >= dl_max:
                dl_count = 0
                # delete old files, if older 2 minutes
                delete_old_files(dl_dir, dl_min)
            break


# Create an MQTT client instance
client = mqtt.Client()

# Attach the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
broker = MQTT_BROKER
port = MQTT_PORT

client.connect(broker, port)

# Start the network loop to process incoming and outgoing messages
client.loop_forever()
