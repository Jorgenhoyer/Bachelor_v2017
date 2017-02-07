#!/usr/bin/env python

#Dette programmet leser av innkommende bytes paa serialport ttyACM0,
#dekoder dataen og skriver den til en fil med et timestamp.

from time import gmtime, strftime
from time import sleep
import Adafruit_BBIO.GPIO as GPIO #import GPIO Library
import serial
import time
f = open('ser_logg.txt', 'w')
ser = serial.Serial("/dev/ttyACM0", baudrate=115200, stopbits=1, parity="N", timeout=1)
outPin_rst="P9_12"                #set outPin for  Reset to "P9_12"

GPIO.setup(outPin_rst,GPIO.OUT)   #make outPin_rst an Output

while True:
    tid = strftime("%Y-%m-%d %H:%M:%S")
    in_data = ser.readline()
    dekodet = in_data.decode('utf8')
    if (ser.inWaiting()>0):
        print(tid)
        print(dekodet)
        f.write(tid)
        f.write(dekodet) #skriv til fil
        f.write('\n\r')
        f.close()
        f=open('ser_logg.txt', 'a')

ser.close()
ser.flush()
ser.open()
