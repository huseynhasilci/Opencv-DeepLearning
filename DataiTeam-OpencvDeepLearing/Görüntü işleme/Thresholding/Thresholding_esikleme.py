# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 09:49:00 2021

@author: husey
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('img',img)
plt.figure()
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()

#esikleme

_,thres_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thres_img,cmap='gray')
plt.axis('off')
plt.show()

#ADAPIVE THRESHOLD
thres_img2= cv2.adaptiveThreshold(img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=8)
plt.figure()
plt.imshow(thres_img2,cmap='gray')
plt.axis('off')
plt.show()

