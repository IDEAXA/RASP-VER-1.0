import ibmiotf.device
import time,json
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27

def myCommandCallback(cmd):
  print("Command received: %s" % cmd.data)


param = {                                     #change all the parameter frrom IBM watson iot device portal
    "org": "3n4830",
    "type": "NODE",
    "id": "MODBUS2k18",
    "auth-method": "token",
    "auth-token": "_hcXXOFbYdj+4Q)oZZ",
    "clean-session":"true"
        }
client = ibmiotf.device.Client(param)
client.connect()
client.commandCallback = myCommandCallback
myQosLevel=2
while 1:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    payload = {
        "HUMIDITY": humidity,
        "TEMPERATURE": temperature
    }
    temp = client.publishEvent("status", "json", json.dumps(payload), myQosLevel)
    print("data sending -:"+str(payload)+ " " + str(temp))
    time.sleep(1)