# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:50:35 2021

@author: husey
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

coin = cv2.imread('coins.jpg')
plt.figure()
plt.imshow(coin,cmap='gray')
plt.axis('off')

#lpf: bluring
coin_blur = cv2.medianBlur(coin, ksize=13)
plt.figure()
plt.imshow(coin_blur,cmap='gray')
plt.axis('off')

#######################################
coin_gray = cv2.cvtColor(coin_blur,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(coin_gray,cmap='gray')
plt.axis('off')


#binary threshold 
ret, coin_thres = cv2.threshold(coin_gray, thresh=75, maxval=255, type= cv2.THRESH_BINARY)
plt.figure()
plt.imshow(coin_thres,cmap='gray')
plt.axis('off')

#kontur 
contours,hierarchy=cv2.findContours(coin_thres.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1: #external
        cv2.drawContours(coin, contours, i,(0,255,0),10)


plt.figure()
plt.imshow(coin,cmap='gray')
plt.axis('off')

#######################Watershed####################################

coin = cv2.imread('coins.jpg')
plt.figure()
plt.imshow(coin,cmap='gray')
plt.axis('off')

#lpf: bluring
coin_blur = cv2.medianBlur(coin, ksize=13)
plt.figure()
plt.imshow(coin_blur,cmap='gray')
plt.axis('off')

coin_gray = cv2.cvtColor(coin_blur,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(coin_gray,cmap='gray')
plt.axis('off')

#binary threshold 
ret, coin_thres = cv2.threshold(coin_gray, thresh=65, maxval=255, type= cv2.THRESH_BINARY)
plt.figure()
plt.imshow(coin_thres,cmap='gray')
plt.axis('off')

#acilma
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(coin_thres, op=cv2.MORPH_OPEN, kernel=kernel,iterations=2)
plt.figure()
plt.imshow(opening,cmap='gray')
plt.axis('off')


# nesneler arasi distance bulalim
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5) 
plt.figure()
plt.imshow(dist_transform,cmap='gray')
plt.axis('off')

#resmi kucult ondeki nesneleri bulmak icin

ret, sure_foreground = cv2.threshold(dist_transform, 0.4*np.max(dist_transform), 255, 0)

plt.figure()
plt.imshow(sure_foreground,cmap='gray')
plt.axis('off')

#arka plan icin resmi buyut
sure_background = cv2.dilate(opening,kernel,iterations=1)
sure_foreground = np.uint8(sure_foreground)

unknown = cv2.subtract(sure_background, sure_foreground)
plt.figure()
plt.imshow(unknown,cmap='gray')
plt.axis('off')

# baglanti

ret, marker = cv2.connectedComponents(sure_foreground)
marker = marker+1
marker[unknown==255] = 0
plt.figure()
plt.imshow(marker,cmap='gray')
plt.axis('off')

#havza watershed

marker = cv2.watershed(coin,marker)
plt.figure()
plt.imshow(marker,cmap='gray')
plt.axis('off')

#contours tekrardan contur cizme

#kontur 
contours,hierarchy=cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1: #external
        cv2.drawContours(coin, contours, i,(255,0,0),10)


plt.figure()
plt.imshow(coin,cmap='gray')
plt.axis('off')



































