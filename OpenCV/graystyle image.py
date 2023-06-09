from cv2 import*
import numpy as np

img=cv2.imread('img.jpg',1)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#cv2.imshow('image', img)
#cv2.waitKey(1)
cv2.imshow('image', gray)
cv2.waitKey(1)
