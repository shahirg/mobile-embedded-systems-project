from picamera import PiCamera
from time import sleep
import face_recognition
import numpy as np
# file to lockf
file = input("Enter file path of file you want to lock:")

#images
upload = input('Would you like to upload images or take them now: (y/n)')
#upload

if upload == 'y':
    upload_path = '/home/pi/Documents/test/sg0.jpg'
    #upload_path = input("Enter file path of image 1:")
    known_image = face_recognition.load_image_file(upload_path)
else:

    sleep(1)
    cam = PiCamera()

    cam.start_preview()
    #cam.rotation = 180
    sleep(3)
    cam.capture(f'/home/pi/Documents/test/known.jpg')
    known_image = face_recognition.load_image_file('/home/pi/Documents/test/known.jpg')

known_encoding = face_recognition.face_encodings(known_image)[0]
print(repr(known_encoding))

with open('/home/pi/Documents/test/encoding.txt', 'w') as f:
   f.write(np.array_repr(known_image))

#np.savetxt('/home/pi/Documents/test/encoding2.txt', known_image.reshape(known_image.shape[0],-1))

sleep(5)

from DstTst import check_dist
from gpiozero import MotionSensor

pir = MotionSensor(4)

cam = PiCamera()



while(True):
    pir.wait_for_motion()
    print("Motion detected")

    check_dist()
    cam.start_preview()
    cam.rotation = 180

    sleep(5)
    cam.capture(f'/home/pi/Documents/test/unknown.jpg')
    cam.stop_preview()
    break
    sleep(2)
    #pir.wait_for_no_motion()

    print("Motion stopped")

unknown_image = face_recognition.load_image_file('/home/pi/Documents/test/unknown.jpg')
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([known_encoding], unknown_encoding)
print(results)
if(results[0] == True):
    print('unlocked')
else:
    print('still locked')