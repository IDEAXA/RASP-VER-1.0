import Adafruit_DHT
import pika
import json
import time
from termcolor import colored

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27

AMQP_URL = ""
AMQP_QUEUE = ""
AMQP_EXCHANGE = ""
AMQP_ROUTING_KEY = ""
connection = pika.BlockingConnection(pika.ConnectionParameters(host=AMQP_URL))
channel = connection.channel()
channel.queue_declare(queue=AMQP_QUEUE)

while 1:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    payload = {
        "HUMIDITY": humidity,
        "TEMPERATURE": temperature
    }
    channel.basic_publish(exchange=AMQP_EXCHANGE, routing_key=AMQP_ROUTING_KEY, body=json.dumps(payload))
    print(colored("PUBLISHING  DATA TO AMQP-:" + str(payload), "green"))
    time.sleep(1)





