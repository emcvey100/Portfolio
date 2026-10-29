from cv2 import*
import numpy as np

img=cv2.imread('img.jpg',1)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Gray Scale Image", gray)
#cv2.waitKey(0)

clahe = cv2.createCLAHE(
    clipLimit=3,
    tileGridSize=(10,10)
    )
gray = clahe.apply(gray)

#cv2.imshow("After apply CLAHE", gray)
#cv2.waitKey(0)



faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv2.CASCADE_SCALE_IMAGE
    )
print(f"Found {len(faces)} faces!")

for (x, y, w, h) in faces:
    cv2.rectangle(
        img,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),2
        )

cv2.imshow("Faces found", img)
cv2.waitKey(0)
