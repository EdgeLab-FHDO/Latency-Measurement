from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import cv2 as cv
import time
import csv
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

'''
def millis():
    dt = datetime.now()-start_time
    ms = (dt.days*24*60*60 +dt.seconds)+1000+dt.microseconds/1000.0
    return ms
'''
def led_glow():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
    while True:
        GPIO.output(8, GPIO.HIGH) # Turn on
        sleep(1) # Sleep for 1 second
        GPIO.output(8, GPIO.LOW)
        sleep(1)# Turn off

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
    

time_on = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
print("Starting the setup at ",time_on)
thresholdRes = 100
resistance = thresholdRes + 1
while True:    
    i2c = busio.I2C (board.SCL, board.SDA)
    time_on_sensr = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
    print("Sensor read the data at ",time_on_sensr)
    ads = ADS.ADS1115 (i2c)
    voltageMax = 3.3
    chan0 = AnalogIn (ads, ADS.P0)
    time_on_brd = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]   ## to check
    print("ADC got the value at ",time_on_brd)
    # LED Blinking and detection time
    led_glow()
    Screen_detection()
    
    if (last_res>2000 and resistance<20):
        print("Resistance Now is ", resistance,'Ohms')
    
    '''
    with open('Setup_latency.csv','a') as data_log:
        logger = csv.writer(data_log)
        logger.writerow([Monitor_name,wr_time,avg_exec])
        data_log.close()
'''
    