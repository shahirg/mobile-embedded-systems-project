import face_recognition
known_image = face_recognition.load_image_file('/home/pi/Documents/test/sg0.jpg')
#for i in range(1):
#    known_image.append(face_recognition.load_image_file(f'sg{i}.jpg'))

unknown_image = face_recognition.load_image_file('/home/pi/Documents/test/sg4.jpg')

print('load done')
#sg_encoding = []
#for i in range(1):
#    sg_encoding.append(face_recognition.face_encodings(known_image[i])[0])
sg_encoding = face_recognition.face_encodings(known_image)[0]
print(len(sg_encoding))
print('hi')
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
print(len(unknown_encoding))
print('hi2')
results = face_recognition.compare_faces([sg_encoding], unknown_encoding)
print(results)
print('unlock')