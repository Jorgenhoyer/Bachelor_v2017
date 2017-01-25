#!/usr/bin/env python
##Open cc2650 bootloader backdoor, via Beaglebone Green, by Jorgen Hoyer##
#Basert paa ccfg innstillinger fra JelmerT sin guide om flashing av image på cc13xx/cc26xx via USB

import Adafruit_BBIO.GPIO as GPIO #import GPIO Library

outPin_rst="P9_12"                #set outPin for  Reset to "P9_12"
outPin_sel="P9_14"                #set outPin for Select to "P9_14"

GPIO.setup(outPin_rst,GPIO.OUT)   #make outPin_rst an Output
GPIO.setup(outPin_sel,GPIO.OUT)         #make outPin_sel an Ouput

from time import sleep                  #so we can use delays
for i in range(0,1):                    #loop 1 time
    GPIO.output(outPin_sel, GPIO.LOW)
    sleep(1)
    GPIO.output(outPin_rst, GPIO.LOW)   # Set outPin_rst  LOW (Active)

    sleep(1)                            #Pause
    GPIO.output(outPin_rst, GPIO.HIGH)  #Set outPin_rst HIGH  (Inactive)
    sleep(1)
    GPIO.output(outPin_sel, GPIO.HIGH)  #Set outPing_sel HIGH (Inactive)
    sleep(1)                            #Wait
GPIO.cleanup()                          #Release your pins
