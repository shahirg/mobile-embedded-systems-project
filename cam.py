from picamera import PiCamera
from time import sleep

def take_picture(file_path, rotation=False, wait_time=5):
    camera = PiCamera()
    if(rotation):
        camera.rotation = 180

    camera.start_preview()
    sleep(wait_time)

    camera.capture(file_path)

    camera.stop_preview()
    camera.close()