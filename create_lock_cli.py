from cam import take_picture
from time import sleep
from encryption import generate_key, encrypt
import face_recognition as fr
import numpy as np

PROJECT_DIR = '/home/pi/Documents/test/'
# file to lock
file_encrypt = input("Enter file path of file you want to encrypt:")

#images
upload = input('Would you like to upload images or take them now: (y/n)')


if upload == 'y':
    upload_path = '/home/pi/Documents/test/sg1.jpg'
    #upload_path = input("Enter file path of image 1:")
    known_image = fr.load_image_file(upload_path)
else:
    sleep(1)
    take_picture(file_path=f'{PROJECT_DIR}known.jpg')
    known_image = fr.load_image_file(f'{PROJECT_DIR}known.jpg')

try:
    known_encoding = fr.face_encodings(known_image)[0]
    print(repr(known_encoding))
except(IndexError):
    print('Face not detected')
    exit()


with open(f'{PROJECT_DIR}encoding.txt', 'w') as f:
   f.write(np.array_repr(known_encoding))

key = generate_key(file_path=f'{PROJECT_DIR}mykey.key')
encrypt(key=key,file_path=file_encrypt)


#np.savetxt('/home/pi/Documents/test/encoding2.txt', known_image.reshape(known_image.shape[0],-1))

# sleep(5)

# from distance import get_distance
# from gpiozero import MotionSensor

# pir = MotionSensor(4)

# while(True):
#     pir.wait_for_motion()
#     print("Motion detected")
#     sleep(1)
#     get_distance()
#     sleep(1)
#     take_picture(file_path='/home/pi/Documents/test/unknown.jpg')
#     break

# unknown_image = face_recognition.load_image_file('/home/pi/Documents/test/unknown.jpg')
# try:
#     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
# except(IndexError):
#     print('No Face Detected')
#     exit()
# results = face_recognition.compare_faces([known_encoding], unknown_encoding)
# print(results)
# if(results[0] == True):
#     print('unlocked')
# else:
#     print('still locked')