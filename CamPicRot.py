from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.start_preview()
cam.rotation = 180
sleep(5)
for i in range(5):
    cam.capture(f'/home/pi/Documents/test/sg{i}.jpg')
    sleep(2)
cam.stop_preview()