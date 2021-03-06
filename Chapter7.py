import cv2
import numpy as np

def empty(a):
    pass

#Trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", (640,240))
cv2.createTrackbar("Hue Min", "TrackBars", 43 , 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 170 , 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 30 , 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 231 , 255, empty)
cv2.createTrackbar("Valu Min", "TrackBars", 0 , 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255 , 255, empty)


while True:
    path = "lena.png"
    img = cv2.imread(path)
    #img = cv2.resize(img1, (900, 640))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    #print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower= np.array([h_min, s_min, v_min])
    upper= np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask= mask) 

    cv2.imshow("Image", img)
    #cv2.imshow("HSV", hsv)
    #cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(1)

