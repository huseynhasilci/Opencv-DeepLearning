# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:33:28 2021

@author: husey
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

#bir tane frame oku

ret,frame = cap.read()

if ret == False:
    print('Uyari')

#detection
#while loopa almadik cunku il once tek bir frame uzerinde tespitini yapip daha sonrasinda tracking yapacagiz
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_rect = face_cascade.detectMultiScale(frame)

(face_x,face_y,w,h) = tuple(face_rect[0])

track_window = (face_x,face_y,w,h)#meanshift algoritması girdisi

#region of intererst

roi = frame[face_y: face_y+h, face_x: face_x+w]
#roi = face

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0,180]) #takip icin histogram gerekli
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

#takip icin gerekli durdurma kriterleri
#count  = hesaplanacak maksimum oge sayisi
#eps = degisiklik(epsilon)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,5,1)

while True:
    
    ret,frame = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #histogramı bir goruntude bulmak icin kullanilir
        #piksel karsilastirma
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

        ret,track_window = cv2.meanShift(dst, track_window, term_crit)

        x,y,w,h = track_window
        
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),5)

        cv2.imshow('Takip',img2)

        if cv2.waitKey(0) & 0xFF==ord('q'):
            break


cap.release()
cv2.destroyAllWindows()





