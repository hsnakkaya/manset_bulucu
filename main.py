import numpy as np
from matplotlib import pyplot as plt
import cv2
import random


filename = 'images/safak.jfif'
img_original = cv2.imread(filename)
height, width, channels = img_original.shape
img_process = img_original.copy()

# img_edited = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(img_process, (7, 1), 0)
edged = cv2.Canny(blur, 0, 100)
dilated = cv2.dilate(edged, np.ones((11, 11)))

contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i, contour in enumerate(contours):
    if 1:
        rect = cv2.boundingRect(contour)
        x, y, w, h = [r for r in rect]
        b, g = random.sample(range(0, 255), 2)
        cv2.rectangle(img_original, (x, y), ((x + w), (y + h)), (b, g, 255), 10)

resized = cv2.resize(img_original, (int(width/4), int(height/4)))
resized1 = cv2.resize(blur, (int(width/4), int(height/4)))
resized2 = cv2.resize(edged, (int(width/4), int(height/4)))
resized3 = cv2.resize(dilated, (int(width/4), int(height/4)))

cv2.imshow('resized', resized)
cv2.imshow('resized1', resized1)
cv2.imshow('resized2', resized2)
cv2.imshow('resized3', resized3)


cv2.waitKey(0)
cv2.destroyAllWindows()
