import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import time

filename = 'images/safak.jfif'
img_original = cv2.imread(filename, 0)
img_process = img_original.copy()

(thresh, img_bin) = cv2.threshold(img_process, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img_process = 255-img_bin

height, width = img_original.shape
x =1

def nothing(x):
    pass


cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('edged', 'image', 0, 100, nothing)
cv2.createTrackbar('blur', 'image', 0, 50, nothing)
cv2.createTrackbar('dilated', 'image', 0, 50, nothing)
cv2.createTrackbar('blur2', 'image', 0, 50, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar('0 : OFF \n1 : ON', 'image', 0, 2, nothing)

while 1:

    time.sleep(0.1)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        x = 1
        b = cv2.getTrackbarPos('blur', 'image')
        b = (b*2)+1
        e = cv2.getTrackbarPos('edged', 'image')
        d = cv2.getTrackbarPos('dilated', 'image')
        d = (d * 2) + 1
        f = cv2.getTrackbarPos('blur2', 'image')
        f = (e * 2) + 1

        edged = cv2.Canny(img_original, 0, e)
        blur = cv2.GaussianBlur(edged, (b, b), 0)
        dilated = cv2.dilate(blur, np.ones((d, d)))
        blur2 = cv2.GaussianBlur(dilated, (f, f), 0)

        vis = np.concatenate((img_original, edged), axis=1)
        vis = np.concatenate((vis, blur), axis=1)
        vis = np.concatenate((vis, dilated), axis=1)
        vis = np.concatenate((vis, blur2), axis=1)

        resized = cv2.resize(vis, (int(width / 5)*5, int(height / 5)))
        cv2.imshow('image', resized)

    elif s == 1:

        while x == 1:
            b = cv2.getTrackbarPos('blur', 'image')
            b = (b * 2) + 1
            e = cv2.getTrackbarPos('edged', 'image')
            d = cv2.getTrackbarPos('dilated', 'image')
            d = (d * 2) + 1
            blur = cv2.GaussianBlur(img_process, (b, b), 0)
            edged = cv2.Canny(blur, 0, e)
            dilated = cv2.dilate(edged, np.ones((d, d)))

            contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for i, contour in enumerate(contours):
                if 1:
                    rect = cv2.boundingRect(contour)
                    x, y, w, h = [r for r in rect]
                    cv2.rectangle(img_original, (x, y), ((x + w), (y + h)), (255, 0, 0), 10)

            resized3 = cv2.resize(img_original, (int(width / 4), int(height / 4)))
            cv2.imshow('image', resized3)
            x = 0

    else:
        x = 1
        resized2 = cv2.resize(img_original, (int(width / 4), int(height / 4)))
        cv2.imshow('image', resized2)

cv2.destroyAllWindows()
