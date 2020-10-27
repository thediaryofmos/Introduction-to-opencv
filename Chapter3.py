import cv2
import numpy as np

img = cv2.imread("lambo.png")
print(img.shape)
imgresize = cv2.resize(img, (600, 200)) #Resize img(), widthxheight
print(imgresize.shape)

imgcrop = img[0:200, 300:600] #Heightxwidth

cv2.imshow("Lamborgini", img)
cv2.imshow("Resized", imgresize)
cv2.imshow("Cropped", imgcrop)
cv2.waitKey(0)