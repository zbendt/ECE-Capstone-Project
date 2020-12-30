from picamera import PiCamera
from time import sleep

camera = PiCamera()

while True:
    camera.start_preview()
    sleep(30)
    camera.stop_preview()
    sleep(1)