import os
from multiprocessing import Process
import time
import RPi.GPIO as GPIO
b = 29
g = 11
r = 12
shut_down = 16
reboot = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(shut_down, GPIO.IN)
GPIO.setup(reboot, GPIO.IN)
GPIO.setup(r,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
def initial_boot():
    GPIO.output(r, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(r, GPIO.LOW)
    time.sleep(0.1)

def middle_boot():
    GPIO.output(b, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(b, GPIO.LOW)
    time.sleep(0.5)

def final_boot():
    GPIO.output(g, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(g, GPIO.LOW)
    time.sleep(1)
def device_alive():
    GPIO.output(g, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(g, GPIO.LOW)
    time.sleep(10)
def led_run():
    for x in range(30):
        initial_boot()
    for y in range(5):
        middle_boot()
    for z in range(3):
        final_boot()
    while 1:
        device_alive()

def button_read():
    while 1:
        #print("inti button")
        button_state1 = GPIO.input(shut_down)
        button_state2 = GPIO.input(reboot)
        #print(button_state1,button_state2)
        if button_state1 == 1:
            print("Wait Shuting down")
            time.sleep(5)
            initial_boot()
            os.system("sudo shutdown -h now")
        if button_state2 == 1:
            print("Wait Rebooting Now")
            time.sleep(2)
            os.system("sudo shutdown -r now")

if __name__ == '__main__':
    p1 = Process(target=button_read)
    p2 = Process(target=led_run)
    p1.start()
    p2.start()

