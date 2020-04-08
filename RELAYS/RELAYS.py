import time
import RPi.GPIO as GPIO
r1 = 36 # relay 1
r2 = 37 # relay 2
r3 = 38 # relay 3
r4 = 40 # relay 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)
GPIO.setup(r4,GPIO.OUT)
while True:
    GPIO.output(r1,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(r1,GPIO.LOW)
    time.sleep(1)
    GPIO.output(r2,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(r2,GPIO.LOW)
    time.sleep(1)
    GPIO.output(r3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(r3,GPIO.LOW)
    time.sleep(1)
    GPIO.output(r4,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(r4,GPIO.LOW)
    time.sleep(1)

