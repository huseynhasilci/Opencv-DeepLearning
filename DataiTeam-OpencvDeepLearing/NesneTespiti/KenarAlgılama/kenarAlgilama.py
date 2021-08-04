# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:41:38 2021

@author: husey
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('london.jpg',0)
plt.figure()
plt.imshow(img,cmap='gray')
plt.axis('off')
#plt.title('')

edges = cv2.Canny(image=img,threshold1=0,threshold2=255 )

plt.figure()
plt.imshow(edges,cmap='gray')
plt.axis('off')

median_val = np.median(img)
print(median_val)

low = int(max(0,(1-0.33)*median_val)) # alt threshold
high = int(min(255,(1+0.33)*median_val)) #ust threshold

print(low)
print(high)

edges = cv2.Canny(image=img,threshold1=low,threshold2=high )

plt.figure()
plt.imshow(edges,cmap='gray')
plt.axis('off')


#blur 

blurred_img = cv2.blur(img,ksize=(4,4))
plt.figure()
plt.imshow(blurred_img,cmap='gray')
plt.axis('off')

median_val = np.median(blurred_img)
print(median_val)

low = int(max(0,(1-0.33)*median_val)) # alt threshold
high = int(min(255,(1+0.33)*median_val)) #ust threshold

print(low)
print(high)

edges = cv2.Canny(image=blurred_img,threshold1=low,threshold2=high )

plt.figure()
plt.imshow(edges,cmap='gray')
plt.axis('off')



































