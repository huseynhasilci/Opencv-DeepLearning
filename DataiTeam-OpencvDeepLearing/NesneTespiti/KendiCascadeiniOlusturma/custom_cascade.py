# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:30:02 2021

@author: husey
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "cascade.xml"
object_name = 'kalemUcu'

frameWidth = 280
frameHeight = 360

color = (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):pass

#trackbar
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", frameWidth, frameHeight)
cv2.createTrackbar("Scale", "Sonuc", 400, 1000, empty)
cv2.createTrackbar("Neigbor", "Sonuc", 4, 50, empty)

#cascade classier
cascade = cv2.CascadeClassifier("cascade.xml")

while True:
    
    success,img = cap.read()
    if success:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        #detection parameters
        scaleVal = 1+(cv2.getTrackbarPos("Scale", "Sonuc")/1000)
        neigbor = cv2.getTrackbarPos("Neigbor", "Sonuc")
        
        #detection
        rects = cascade.detectMultiScale(gray,scaleVal,neigbor)
    
        for (x,y,w,h) in rects:
    
            cv2.rectangle(img, (x,y),(x+w,y+h), color,3)
            cv2.putText(img, object_name, (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color,2)
    
        cv2.imshow('Sonuc',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()












