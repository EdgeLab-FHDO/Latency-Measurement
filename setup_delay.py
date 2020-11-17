from gpiozero import LED
import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import csv
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import statistics as st

list_time = []
resist_time=[]
rest = []
def Screen_detection():    
    resistance = thresholdRes + 1 # dummy condition
    while resistance > thresholdRes:
        resistanceRaw = chan0.voltage / (voltageMax - chan0.voltage) * 10
        if resistanceRaw > 0:
            resistance = resistanceRaw            
        time.sleep(0.001)
        print ("Resistance value:", resistance)
    exec_time = time.time() - time_on_led1
    list_time.append(exec_time)
    rest.append(int(resistance))
    time_to_read_led = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
    print("LED read by light sensor at ",time_to_read_led)
    avg_exec = str(st.mean(list_time))
    print("Execution time is ",avg_exec)
    #avg_exec = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
    #print("Resistance detected to drop severely at ",avg_exec)
    return avg_exec         
   
def resistance_time():
    
    for zz in (range(1,len(rest))):                  
        if((rest[zz-1]-rest[zz]>50) and (rest[zz]<105 or rest[zz]>0)):
            time_det = time.time()-time_on_led1
            resist_time.append(time_det)
            resistance_time = str(st.mean(resist_time))
            resis = rest[zz]
            print("Resistance Now is ", resis,'Ohms') 
            print("Delta_Res_time ",resistance_time)
            #time_on_resis = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
            #print("Resistance detected to drop severely at ",time_on_resis)
            return resistance_time                  
    
########################################    
######### Code Initilization ###########
########################################    
time_on = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
print("Starting the setup at ",time_on)
thresholdRes = 100
resistance = thresholdRes + 1
led = LED(14)

while True:    
    i2c = busio.I2C (board.SCL, board.SDA)
    time_on_sensr = str(datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3])
    print("Sensor read the data at ",time_on_sensr)
    ads = ADS.ADS1115 (i2c)
    voltageMax = 3.3
    chan0 = AnalogIn (ads, ADS.P0)
    time_on_brd = str(datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3])   ## to check
    print("ADC got the value at ",time_on_brd)
    # LED Blinking and detection time
    time_on_led = str(datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3])
    print("LED on at ",time_on_led)    
    time_on_led1 = time.time()
    led.on()
    avg_exec = Screen_detection() 
    #time.sleep(1)
    led.off()
    time.sleep(1)
    time_on_resis=resistance_time()     
    time_end = str(datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3])   ## to check
    print("Session complete at ",time_end)
    
    
    with open('Setup_latency.csv','a') as data_log:
        logger = csv.writer(data_log)
        
        logger.writerow([time_on,time_on_sensr,time_on_brd,time_on_led,avg_exec,time_on_resis,time_end])
        data_log.close()

    
