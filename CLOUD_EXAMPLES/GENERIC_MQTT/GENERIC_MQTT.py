import time
import json
import Adafruit_DHT
import paho.mqtt.client as mqtt
from termcolor import colored

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27

MQTT_USR =""
MQTT_PASS =""
MQTT_URL = ""
MQTT_PORT =""
TOPIC_SEND = ""
MQTT_QOS = ""
MQTT_client = mqtt.Client()
MQTT_client.username_pw_set(MQTT_USR, MQTT_PASS)
MQTT_client.connect(MQTT_URL, MQTT_PORT)
print(colored("SUCCESFULLY CONNECTED TO MQTT BROKER","green"))
while 1:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    payload = {
        "HUMIDITY": humidity,
        "TEMPERATURE": temperature
    }
    MQTT_client.publish(topic=TOPIC_SEND, payload=payload,qos=MQTT_QOS)
    print(colored("PUBLISHING  DATA TO MQTT-:" + str(payload), "green"))
    time.sleep(1)

