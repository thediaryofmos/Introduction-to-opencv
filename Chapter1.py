import cv2
"""
img = cv2.imread('lena.png')

cv2.imshow("Output", img)
cv2.waitKey(0)
"""


#Video Capture
"""
cap = cv2.VideoCapture("Opening.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

##Using Webcam

cap = cv2.VideoCapture(0)
cap.set(3, 640) #Length id is 3
cap.set(4,480)  #Width id is 4
cap.set(10,100) #Brightness id is 10

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break