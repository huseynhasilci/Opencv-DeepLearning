# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:52:35 2021

@author: husey
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('datai_team.jpg',0)
plt.figure()
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.title('Original Img')
plt.show()

#erozyon

kernel = np.ones((5,5),dtype = np.uint8)
result = cv2.erode(img,kernel,iterations = 1)

plt.figure()
plt.imshow(result,cmap='gray')
plt.axis('off')
plt.title('Erozyon Img')
plt.show()

#genisleme
result2 = cv2.dilate(img,kernel,iterations = 1) 

plt.figure()
plt.imshow(result2,cmap='gray')
plt.axis('off')
plt.title('Genisleme Img')
plt.show()
#noise
whiteNoise = np.random.randint(0,2,size=img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure()
plt.imshow(whiteNoise,cmap='gray')
plt.axis('off')
plt.title('White noise Img')

noise_img = whiteNoise+img
plt.figure()
plt.imshow(noise_img,cmap='gray')
plt.axis('off')
plt.title('Img with white noise')

# acilma
opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure()
plt.imshow(opening,cmap='gray')
plt.axis('off')
plt.title('Acilma ')


#black noise
blackNoise = np.random.randint(0,2,size=img.shape[:2])
blackNoise = blackNoise*-255
plt.figure()
plt.imshow(blackNoise,cmap='gray')
plt.axis('off')
plt.title('Black noise Img')

blackNoiseImg = blackNoise+img
blackNoiseImg[blackNoiseImg<=-245] = 0

plt.figure()
plt.imshow(blackNoiseImg,cmap='gray')
plt.axis('off')
plt.title('Img with Black Noise')


#kapatma

closing = cv2.morphologyEx(blackNoiseImg.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.imshow(closing,cmap='gray')
plt.axis('off')
plt.title('Closing kAPAMA')

# gradient

gradient = cv2.morphologyEx(img.astype(np.float32),cv2.MORPH_GRADIENT,kernel)

plt.figure()
plt.imshow(gradient,cmap='gray')
plt.axis('off')
plt.title('Gradient')




















