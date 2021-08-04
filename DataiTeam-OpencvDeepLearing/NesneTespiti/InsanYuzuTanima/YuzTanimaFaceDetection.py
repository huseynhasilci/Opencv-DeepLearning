# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:42:28 2021

@author: husey
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

einstein = cv2.imread('einstein.jpg',0) 
plt.figure()
plt.imshow(einstein,cmap='gray')
plt.axis('off')

#siniflandirici
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y),(w+x,h+y), (255,255,255),10)
plt.figure()
plt.imshow(einstein,cmap='gray')
plt.axis('off')

#######################barca############################,
barce = cv2.imread('barcelona.jpg',0) 
plt.figure()
plt.imshow(barce,cmap='gray')
plt.axis('off')

face_rect = face_cascade.detectMultiScale(barce,minNeighbors=7)

for (x,y,w,h) in face_rect:
    cv2.rectangle(barce, (x,y),(w+x,h+y), (255,255,255),10)
plt.figure()
plt.imshow(barce,cmap='gray')
plt.axis('off')

cap = cv2.VideoCapture(0)

while True:
    
    ret,frame = cap.read()

    if ret: 
        face_rect = face_cascade.detectMultiScale(frame,minNeighbors=7)
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y),(w+x,h+y), (255,255,255),10)
        cv2.imshow('face detect',frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()








