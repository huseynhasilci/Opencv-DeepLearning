# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:09:15 2021

@author: husey
"""
import cv2
import numpy as np
from collections import deque

#nesne merkezini depolayacak veri tipi
buffer_size = 16

pts = deque(maxlen=buffer_size)

#mavi renk araligi HSV
blueLower = (84,98,0)
blueUpper = (179,255,255)

#capture

cap = cv2.VideoCapture(0)
cap.set(3,960)#height
cap.set(4,480)#width


while True:
    
    success,imgOriginal = cap.read()

    if success:
        
        #blur
        blurred = cv2.GaussianBlur(imgOriginal, ksize=(11,11), sigmaX=0)
        
        #hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        #cv2.imshow("HSV Image",hsv)
        #mavi icin maske olustur
        mask = cv2.inRange(hsv, lowerb=blueLower, upperb=blueUpper)
        #maskenin etrafinda kalan gurultuleri sil 
        mask = cv2.erode(mask,None,iterations=2)
        mask = cv2.dilate(mask,None,iterations=2)
        #cv2.imshow("mask Image",mask)
        #kontur = 
        (_,contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center = None
        
        if len(contours) >0:
            #en buyuk konturu al
            c= max(contours,key=cv2.contourArea) 
            #dikdortgene cevir
            rect = cv2.minAreaRect(c)
            
            ((x,y),(width,height),rotation) = rect
            s = 'x:{}, y:{}, width:{}, height:{},rotation:{}'.format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)
            #kutucuk
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            #moment
            M = cv2.moments(c)
            center = (int(M['m10']/M['m00']),int(M['m01']/M['m00']))
            #konturu cizdir 
            cv2.drawContours(imgOriginal, [box], 0, (0,255,255,2 )
            
            #merkeze 1 tane nokta cizmek                 
            cv2.circle(imgOriginal,center,5,(255,0,255),-1)
                   
            #bilgileri ekrana yazdirma
            cv2.putText(imgOriginal, s, (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL,1 , (255,255,255),2)
        
        #deque
        pts.appendleft(center)
        
        for i in range(1,len(pts)):
            if pts[i-1] is None or pts[i] is None: 
                continue
            cv2.line(imgOriginal,pts[i-1],pts[i],(0,255,0),3)
        cv2.imshow('Orijinal tespit',imgOriginal)
        
        
        
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





















