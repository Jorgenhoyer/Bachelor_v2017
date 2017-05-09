#!/usr/bin/env python

#Dette programmet leser av innkommende bytes paa serialport ttyS*,
#dekoder dataen og skriver den til en fil med et timestamp.

from time import gmtime, strftime
from time import sleep
import Adafruit_BBIO.GPIO as GPIO #import GPIO Library
import serial
import time
f = open('debug-node1.txt', 'wb')
ser = serial.Serial("/dev/ttyS1", baudrate=115200, stopbits=1, parity="N", timeout=1)

while True:
    tid = strftime("%Y-%m-%d %H:%M:%S")
    in_data = ser.readline()
    if (ser.inWaiting()>0):
        #print ('Node1:\n')
        #print(tid)
        #print(in_data)
        #f.write('Node1:\n')
        f.write(tid)
        f.write('\n')
        f.write(in_data)
        f.write('\n')

f.close()
ser.close()
ser.flush()
