import cv2
import numpy as mp
import os
file = cv2.VideoCapture(r"Open CV\video for lesson 6.mp4")
background = 0
for i in range(60):
     return_value, background = file.read()
     if return_value == False:
          continue

while file.isOpened():
    return_value, image = file.read()
    if return_value == False:
        break
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = mp.array([100, 40, 40])
    upper_red = mp.array([100, 255, 255])
    mask1 = cv2.inRange(HSV, lower_red, upper_red)

    lower_red = mp.array([155, 40, 40])
    upper_red = mp.array([180, 255, 255])
    mask2 = cv2.inRange(HSV, lower_red, upper_red)

    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, mp.ones((3, 3), mp.uint8), iterations = 2)
    mask1 = cv2.dilate(mask1, mp.ones((3, 3), mp.uint8), iterations = 1)
    mask2 = cv2.bitwise_not(mask1)
    Result1 = cv2.bitwise_and(background, background, mask = mask1)
    Result2 = cv2.bitwise_and(image, image, mask = mask2)

    FinalResult = cv2.addWeighted(Result1, 1, Result2, 1, 0)
    cv2.imshow("Result", FinalResult)
    key = cv2.waitKey(10)
    if key == 27:
        break