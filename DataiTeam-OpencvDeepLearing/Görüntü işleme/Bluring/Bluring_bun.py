# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:47:34 2021

@author: husey
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


img = cv2.imread('NYC.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis('off')
plt.title('orijinal')
plt.show()


"""
ortalama bulaniklastirma
"""

dst2 = cv2.blur(img,ksize=(3,3))
plt.figure()
plt.imshow(dst2)
plt.axis('off')
plt.title('ortalama blured')
plt.show()

"""
Gaussian bulanklastirma
"""
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis('off')
plt.title('gaussian blured')
plt.show()


"""
median blur
"""
mb = cv2.medianBlur(img, ksize=3)
plt.figure()
plt.imshow(mb)
plt.axis('off')
plt.title('median blured')
plt.show()

def gaussianNoise(image):
    row,col,ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

img = cv2.imread('NYC.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255 #normalize

plt.figure()
plt.imshow(img)
plt.axis('off')
plt.title('orijinal')
plt.show()

gaussianNoiseImg = gaussianNoise(img)

plt.figure()
plt.imshow(gaussianNoiseImg)
plt.axis('off')
plt.title('Gauss Noisy')
plt.show()

gb2 = cv2.GaussianBlur(gaussianNoiseImg, ksize=(3,3), sigmaX=7)

plt.figure()
plt.imshow(gb2)
plt.axis('off')
plt.title('Gauss Noisy Blur')
plt.show()


def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount  = 0.004
    noisy = np.copy(image)

    num_salt = np.ceil(amount*image.size*s_vs_p)
    coords = [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    num_pepper = np.ceil(amount*image.size*(1-s_vs_p))
    coords = [np.random.randint(0,i-1,int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis('off')
plt.title('Salt Pepper Image')
plt.show()


mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize=3)


plt.figure()
plt.imshow(mb2)
plt.axis('off')
plt.title('Salt Papper Median Blur')
plt.show()















