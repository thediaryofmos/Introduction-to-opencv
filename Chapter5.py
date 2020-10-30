import cv2
import numpy as np

img = cv2.imread("cards.png")
print(img.shape)

imgresize = cv2.resize(img, (392,408))
width,height = 250, 350

cv2.imshow("image", imgresize)
pts1 = np.float32([[136,1], [320,51],[0,246], [233,327]])
pts2 = np.float32([[0,0], [width,0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(imgresize, matrix, (width,height))

cv2.imshow("Output", imgOutput)

cv2.waitKey(0)