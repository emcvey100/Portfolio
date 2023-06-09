import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread("abc.png",1)

decodedObject = pyzbar.decode(img)

#print(decodedObject)

for obj in decodedObject:
    print("data:", obj.data)


cv2.imshow("Image", img)
cv2.waitKey(0)
