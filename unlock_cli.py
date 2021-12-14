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