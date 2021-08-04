# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:12:23 2021

@author: husey
"""

import cv2
import matplotlib.pyplot as plt


def imagePyramid(image,scale=1.5,minSize=(224,224)):
    
    yield image
    
    while True:
        w = int(image.shape[1]/scale)
        
        image = cv2.resize(image,dsize=(w,w))
        
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        
        yield image
        
#img = cv2.imread("husky.jpg")     
#im = imagePyramid(img,1.5,(10,10))      
        
#for i, image in enumerate(im):        
#    print(i)
#    if i == 8:
#       plt.imshow(image) 
        



































