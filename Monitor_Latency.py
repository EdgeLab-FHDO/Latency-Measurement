# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:38:55 2020

@author: Satyam
"""
from tkinter import *
import cv2 as cv
import time
import csv
import statistics as st
import keyboard
import numpy as np
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C (board.SCL, board.SDA)
ads = ADS.ADS1115 (i2c)
voltageMax = 3.3
chan0 = AnalogIn (ads, ADS.P0)
thresholdRes = 100
Monitor_name = str(input("Please enter a name of your current display "))
                   

screen_size=Tk()
width=screen_size.winfo_screenwidth()
height=screen_size.winfo_screenheight()
screen_size.geometry("%dx%d+0+0" %(width,height))
screen_size.configure(background='black')
start_time=0
list_time=[]

def Screen_detection():
    
    
    resistance = thresholdRes + 1 # dummy condition
    while resistance > thresholdRes:
        resistanceRaw = chan0.voltage / (voltageMax - chan0.voltage) * 10
        if resistanceRaw > 0:
            resistance = resistanceRaw            
        time.sleep(0.001)
        #print ("Voltage value:", chan0.voltage, "Resistance value:", resistance)

    exec_time = time.time() - start_time
    list_time.append(exec_time)
       
    print("Execution time is ",exec_time)    
    wr_time=time.strftime('%d-%m-%Y %H:%M:%S')
    avg_exec = str(st.mean(list_time))
    with open('Data_logger.csv','a') as data_log:
        logger = csv.writer(data_log)
        logger.writerow([Monitor_name,wr_time,avg_exec])
    
    data_log.close()
        
    
while True:

        print("Displaying the white screen now")
        screen_size.configure(background='white')
        screen_size.update()
        start_time = time.time()
        Screen_detection()
        print("Displaying the black screen now")
        screen_size.configure(background='black')
        screen_size.update()
        time.sleep(1)
        #break
        
