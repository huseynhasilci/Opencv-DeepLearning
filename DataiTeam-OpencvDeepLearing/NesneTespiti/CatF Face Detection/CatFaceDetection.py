# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:04:01 2021

@author: husey
"""

import cv2 
import matplotlib.pyplot as plt
import numpy as np
import os

files = os.listdir()

img_path = []

for f in files:
    if f.endswith('.jpg'):
        img_path.append(f)
print(img_path)

for i in img_path:
    image = cv2.imread(i)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    detector= cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    
    rects = detector.detectMultiScale(gray,scaleFactor = 1.045,minNeighbors=2)

    for(i,(x,y,w,h)) in enumerate(rects):
        cv2.rectangle(image, (x,y), (x+w,y+h),(0,255,255),2 )
        cv2.putText(image, 'Kedi: {}'.format(i+1), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,255,255))

    cv2.imshow('kedi',image)
    if cv2.waitKey(0)& 0xFF ==ord('q'):
        continue




























