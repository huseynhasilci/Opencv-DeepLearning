# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:27:28 2021

@author: husey
"""

import cv2
import matplotlib.pyplot as plt


def slidingWindow(image,step,ws):
    
    for y in range(0,image.shape[0]-ws[1],step):
        for x in range(0,image.shape[1]-ws[0],step):

            yield(x,y,image[y:y+ws[1],x:x+ws[0]])

#img = cv2.imread('husky.jpg')
#im = slidingWindow(img, 5, (200,150))

#for i,image in enumerate(im):
#    print(i)    
#    if i == 14125:
#        print(image[0],image[1])
#        plt.imshow(image[2])







































