import time
import RPi.GPIO as GPIO
b = 31
g = 37
r = 38
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(r,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
while True:
    GPIO.output(r,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(r,GPIO.LOW)
    time.sleep(1)
    GPIO.output(g,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(g,GPIO.LOW)
    time.sleep(1)
    GPIO.output(b,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(b,GPIO.LOW)
    time.sleep(1)
