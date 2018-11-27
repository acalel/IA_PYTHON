# -*- coding: utf-8 -*-

import cv2
import numpy as np
print(cv2.__version__)

web_cam = cv2.VideoCapture(0)

cascade_src = 'cars.xml'
video_src = 'dataset/video1.avi'
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)   

        font = cv2.FONT_HERSHEY_SIMPLEX            


        color = (255,255,255)
        grosor = 2   
    
        cv2.putText(img, "auto", (x,y), font, 1, color, grosor, cv2.LINE_AA)

      
     

    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break
   

cv2.destroyAllWindows()