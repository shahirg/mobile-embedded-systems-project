from cam import take_picture
from time import sleep
from encryption import generate_key, encrypt
from pick import pick
import face_recognition as fr
import numpy as np

PROJECT_DIR = '/home/pi/Documents/test/'

# file to lock
file_encrypt = input("Enter file path of file to encrypt:")

# upload image or take new
title = "Select Image Upload Option"
options = ['Upload Image of Face', 'Take photo now']
option, index = pick(options, title, indicator='=>')

if index == 0:
    upload_path = input("Enter file path of image:")
    known_image = fr.load_image_file(upload_path)
else:
    sleep(1)
    take_picture(file_path=f'{PROJECT_DIR}known.jpg')
    known_image = fr.load_image_file(f'{PROJECT_DIR}known.jpg')

try:
    # get face encoding
    known_encoding = fr.face_encodings(known_image)[0]
except(IndexError):
    print('Face not detected')
    exit()

# store encoding in text file
with open(f'{PROJECT_DIR}encoding.txt', 'w') as f:
   f.write(np.array_repr(known_encoding))

# encrypt file
key = generate_key(file_path=f'{PROJECT_DIR}mykey.key')
encrypt(key=key,file_path=file_encrypt)
print(f'{file_encrypt} encrypted')