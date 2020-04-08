from picamera import PiCamera
from time import sleep
from datetime import datetime
DateString = "%Y-%m-%d"
TimeString = "%H:%M:%S"
date = str(datetime.now().strftime(DateString))
time = str(datetime.now().strftime(TimeString))
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
camera.capture(str(time)+'.jpg')
sleep(5)
camera.stop_preview()
