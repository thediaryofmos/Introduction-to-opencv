import cv2
import numpy as np

#Defining kernal for Dilation
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("lena.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0) #Guassian Blur

#Canny Edge Detection
imgCanny = cv2.Canny(img, 150, 150)

#Dilating Edges
imgDilation = cv2.dilate(imgCanny,kernel, iterations= 1)

#Image Erosion
imgErosion = cv2.erode(imgDilation, kernel, iterations= 1)

#cv2.imshow("Gray", gray)
#cv2.imshow("Blur", blur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Image Dialation", imgDilation)
cv2.imshow("Image Erosion", imgErosion)
cv2.waitKey(0)