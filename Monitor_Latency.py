# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:38:55 2020

@author: Satyam
"""
from tkinter import *
import cv2 as cv
import time
import keyboard
import numpy as np

### for a variable size full screen blue display
screen_size=Tk()
width=screen_size.winfo_screenwidth()
height=screen_size.winfo_screenheight()
screen_size.geometry("%dx%d+0+0" %(width,height))
screen_size.configure(background='blue')
start_time=0

def Screen_detection():
    video = cv.VideoCapture(0)
    check, frame = video.read()  
    cv.imshow("Window", frame)
    video.release()
    cv.waitKey(0)
    img=cv.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))       
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)         
    lower_range = np.array([0,100,100])
    upper_range = np.array([2,255,255])     
    mask = cv.inRange(hsv, lower_range, upper_range)     
    cv.imshow('image', img)
    cv.imshow('mask', mask)    
    exec_time = time.time() - start_time    
    cv.waitKey(0)
    cv.destroyAllWindows()    
    print("Execution time is ",exec_time)
        
    
### clocks the time at which the display data is sent with 's' button pressed and Camera ON
### this
while True:
    if(keyboard.is_pressed('s')):    
        print("Displaying the blank screen now")
        start_time = time.time()
        #screen_size.mainloop()
        Screen_detection()
    else:
        print("Press s to start")
        time.sleep(5)
        #break
        

### clocks the time at which the white screen is detected by the rPi sensor with green LED blink
#exec_time = time.time() - start_time
#print("Execution time is ",exec_time)

