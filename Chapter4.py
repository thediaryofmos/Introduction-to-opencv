import cv2
import numpy as np

img= np.zeros((512,512,3), np.uint8)
print(img.shape)
#img[:] = 255,0,0  #Coloring the whole image
#Drawing a Line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]), (0,0,255), 3) #img.shap[0] = height, img.shape[1] = width
cv2.rectangle(img,(0,0),(250,350), (13,155,233), cv2.FILLED)
cv2.circle(img,(450,300),50, (255,20,50), 6)
cv2.putText(img, "OPENCV BY OSME", (200,400), cv2.FONT_HERSHEY_COMPLEX, 1, (50,80,200), 1)


cv2.imshow("Image", img)
cv2.waitKey(0)