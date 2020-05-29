import numpy as np
from cv2 import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('image2.jpg')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grayImage, 1.1, 20)
if len(faces)==0:
    print ("no faces found")
else:
    print(faces) 
    print (faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
    cv2.imshow('Image with faces',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()