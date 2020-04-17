import requests
import json
import time
import Adafruit_DHT
from termcolor import colored
HTTP_URL = ""

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27
while 1:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    payload = {
        "HUMIDITY": humidity,
        "TEMPERATURE": temperature
    }
    r = requests.post(url=HTTP_URL, data=json.dumps(payload))
    print(colored("SUCCESFULLY SEND DATA TO AWS_IOT BROKER", "green"))
    print(colored(payload, "green"))
    time.sleep(1)
    response_get = r.text
    print("The response we get :%s" % response_get)
    time.sleep(1)
