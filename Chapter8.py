import cv2
import numpy as np
from stackedImages1 import stackImages

img = cv2.imread("shape.png")
imgContour = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 1)
imgBlank = np.zeros_like(img)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area) 
        if area> 500:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
            per= cv2.arcLength(cnt, True)
            #print(per)
            approx = cv2.approxPolyDP(cnt, 0.02*per, True)
            print(len(approx))
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorners ==3: objType = "Triangle"
            elif objCorners ==4: 
                aspRatio = w/ float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objType = "Square"
                else: objType = "Rectangle"
            elif objCorners ==5: objType = "Pentagon"
            elif objCorners ==6: objType = "Hexagon"
            else: objType = "Circle"
            

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 100, 200), 3)
            cv2.putText(imgContour, objType, (x+(w//2)-10, y+ (h//2)-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255), 2)


canny = cv2.Canny(blur, 50, 50)
getContours(canny)
imgstack = stackImages(1.0, ([img, gray], [blur, canny], [imgBlank, imgContour]))

cv2.imshow("Stack", imgstack)
cv2.waitKey(0)