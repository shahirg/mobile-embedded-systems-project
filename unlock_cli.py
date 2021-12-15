from distance import get_distance
from encryption import decrypt, load_key
from gpiozero import MotionSensor
from cam import take_picture
from time import sleep
from numpy import array
import numpy as np
import face_recognition as fr

PROJECT_DIR = '/home/pi/Documents/test/'

file_decrypt = input("Enter file path of file you want to decrypt:")
file_decrypt = f'{PROJECT_DIR}test_encrypt.txt'

with open(f'{PROJECT_DIR}encoding.txt', 'r') as f:
    encoding = f.read()
    print(encoding)

known_encoding = eval(encoding)

pir = MotionSensor(4)

while(True):
    pir.wait_for_motion()
    print("Motion detected")
    sleep(1)
    get_distance()
    sleep(1)
    take_picture(file_path=f'{PROJECT_DIR}unknown.jpg')
    break


unknown_image = fr.load_image_file(f'{PROJECT_DIR}unknown.jpg')
unknown_encoding = fr.face_encodings(unknown_image)[0]
results = fr.compare_faces([known_encoding], unknown_encoding)
print(results)
if(results[0] == True):
    print('unlocked')
    key = load_key(file_path=f'{PROJECT_DIR}mykey.key')
    decrypt(key=key,file_path=file_decrypt)
else:
    print('still locked')