# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:46:03 2021

@author: husey
"""

import cv2
import numpy as np

def nonMaxiSupression(boxes,probs = None,overlapThreshold=0.3):
    
    if len(boxes) == 0:
        return []
    
    if boxes.dtype.kind =='i':
        boxes = boxes.astype("float")
    
    
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    
    x2 = boxes[:,2]
    y2 = boxes[:,3]
    
    #alani bulalim
    area = (x2-x1+1)*(y2-y1+1)
    
    idxs = y2
    #olasilik degerleri
    if probs is not None:
        idxs = probs
    #indeksi sirala
    idxs = np.argsort(idxs)
    
    pick = [] #secilen kutular
    
    while len(idxs) >0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
    
        #en buyuk ve en kucuk x ve y degerleri
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.maximum(y2[i], y2[idxs[:last]])
    
        #w,h bulmak
        w = np.maximum(0, xx2-xx1+1)
        h = np.maximum(0, yy2-yy1+1)
    
        #overlap 
        overlap = (w*h)/area[:last]
        idxs = np.delete(idxs,np.concatenate(([last],
                                              np.where(overlap>overlapThreshold)[0])))
    
    return boxes[pick].astype('int')
    
    
    
    
    
    
    
    
    
    