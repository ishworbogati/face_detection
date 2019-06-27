# using viola-johns algorithm

import cv2
import numpy as np
import matplotlib.pyplot as plt

# load in color image for face detection
image = cv2.imread('decoded.jpg')

# convert to rbg
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.figure(figsize=(20, 10))
# plt.imshow(gray_img, cmap='gray')
# plt.show()

# load in cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# run the detector on the grayscale image
faces = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(1, 1),
    flags=cv2.CASCADE_SCALE_IMAGE
)


img_with_detections = np.copy(image)
for(x, y, w, h) in faces:
    cv2.rectangle(img_with_detections, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img_with_detections)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.figure(figsize=(20, 10))
# plt.imshow(img_with_detections)
# plt.show()
