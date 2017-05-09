#!/usr/bin/env python

#Dette programmet leser av innkommende bytes paa serialport ttyS*,
#dekoder dataen og skriver den til en fil med et timestamp.

from time import gmtime, strftime
from time import sleep
import Adafruit_BBIO.GPIO as GPIO #import GPIO Library
import serial
import time

f = open('debug-node3.txt', 'wb')
ser = serial.Serial("/dev/ttyS4", baudrate=115200, stopbits=1, parity="N", timeout=1)


while True:
    tid = strftime("%Y-%m-%d %H:%M:%S")
    in_data = ser.readline()
    if (ser.inWaiting()>0):
        #print ('Node3:\n')
        #print(tid)
        #print(in_data)
        #f.write('Node3:\n')
        f.write(tid)
        f.write('\n')
        f.write(in_data)
        f.write('\n')

f.close()
ser.close()
ser.flush()
