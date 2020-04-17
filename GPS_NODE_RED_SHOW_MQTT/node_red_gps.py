import json

import serial
import paho.mqtt.client as mqtt
serial1 = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
print("mqqt connecting")
username = ""
password = ""
mq_client = "12werty"
MQTT_client = mqtt.Client()
MQTT_client.username_pw_set(username,password)
MQTT_client.connect("192.168.43.39", port=1883)
print("mqqt connected")

while 1:
    a = str(serial1.readline())
    data = a.split(",")
    # if data[0] == "b'$GPRMC":  # for old gps
    if data[0] == "b'$GNRMC":  # for new m8n gps
        if data[2] == "A":
            a = data[3]  # raw lat
            b = data[5]  # raw lon
            c = data[7]  # raw speed
            lati = float(a) / 100
            longi = float(b) / 100
            speed = float(data[7]) * 1.852
            lati_int = int(lati)
            longi_int = int(longi)
            raw_lat = float(lati - lati_int) / 60.0
            raw_lon = float(longi - longi_int) / 60.0
            latitude = (lati_int + (raw_lat * 100))
            latitude = (lati_int + (raw_lat * 100))
            longitude = (longi_int + (raw_lon * 100))
            latitude = str(format(latitude, '.6f'))
            longitude = str(format(longitude, '.6f'))
            speed = str(format(speed, '.1f'))
            #print(latitude, longitude, speed + "-Km/h")
            data_gps = {
                "name":"sachin",
                "lat":latitude,
                "lon":longitude,
                "speed":speed
            }
            MQTT_client.publish(topic="gps", payload=json.dumps(data_gps), qos=0)
            print(data_gps)
        if data[2] == "V":
            print("GPS data not Available..")
