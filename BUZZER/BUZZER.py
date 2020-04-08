import time
import RPi.GPIO as GPIO
BUZZER= 31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER,GPIO.OUT)
while True:
    GPIO.output(BUZZER,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER,GPIO.LOW)
    time.sleep(1)

