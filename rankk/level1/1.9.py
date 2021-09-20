# Rankk: Level 1.9 - Do you paint?
# woanmeo11

import cv2, os

os.system('convert rankkix.gif rankkix.png')
img = cv2.imread('rankkix.png')
rows, cols, _ = img.shape

for i in range(rows):
    for j in range(cols):
        r, g, b = img[i, j]
        if r != 255 and g != 255 and b != 255:
            img[i, j] = [0, 0, 0]

cv2.imshow('sol', img)
cv2.waitKey(0)
