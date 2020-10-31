import cv2
import numpy as np


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#img = cv2.imread("lena.png")

cap = cv2.VideoCapture(0)
cap.set(3, 640) #Length id is 3
cap.set(4,480)  #Width id is 4
cap.set(10,100) #Brightness id is 10

while True:
    success, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (200, 30, 60), 2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




##cv2.imshow("Image", img)
##cv2.waitKey(0)