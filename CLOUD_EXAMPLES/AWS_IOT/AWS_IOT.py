import json
import Adafruit_DHT
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from termcolor import colored

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27

ID = "xyz"
AWS_IOT_ARN = ""
AWS_IOT_PORT = ""
certRootPath = "aws_iot_certificates"
AWS_IOT_SEND_TOPIC = ""
myMQTTClient = AWSIoTMQTTClient(ID)
myMQTTClient.configureEndpoint(AWS_IOT_ARN, AWS_IOT_PORT)
myMQTTClient.configureCredentials("{}root-ca.pem".format(certRootPath), "{}cloud.pem.key".format(certRootPath),
                                  "{}cloud.pem.crt".format(certRootPath))
myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
print(colored("CONNECTING TO AWS_IOT BROKER", "green"))
myMQTTClient.connect()
print(colored("SUCCESFULLY CONNECTED TO AWS_IOT BROKER", "green"))
while 1:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    payload = {
        "HUMIDITY": humidity,
        "TEMPERATURE": temperature
    }
    myMQTTClient.publish(AWS_IOT_SEND_TOPIC, json.dumps(payload), 0)
    print(colored("SUCCESFULLY SEND DATA TO AWS_IOT BROKER", "green"))
    print(colored(payload, "green"))
    time.sleep(1)
