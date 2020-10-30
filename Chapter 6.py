import cv2
import numpy as np
from stackedImages1 import stackImages

img = cv2.imread("lena.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


"""
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal StackedImages", imgHor)
cv2.imshow("Vertical StackedImages", imgVer)
"""

imgStack = stackImages(0.7, ([img,img,img,img], [img,gray,img,gray]))
cv2.imshow("StackedImages", imgStack)
cv2.waitKey(0)