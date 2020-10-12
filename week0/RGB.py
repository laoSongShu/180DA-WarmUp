'''
    Citations:
    https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
    https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#exercises
'''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for index in range(1000):
    _, frame = cap.read()
    
    # you need to divide the normal scale by half to convert from 360 to 180
    lower_blue = np.array([130, 40, 0])
    upper_blue = np.array([250, 130, 88])
    
    mask = cv2.inRange(frame,lower_blue,upper_blue)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(cnts) > 0:
        # use the largest contour in the mask to compute the minumum enclosing rectangle
        c = max(cnts, key = cv2.contourArea)
        # from section: bounding rectangle
        x,y,w,h = cv2.boundingRect(c)
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("frame",frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()


