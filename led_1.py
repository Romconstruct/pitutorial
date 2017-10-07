#!/usr/bin/python3

#----------------------------------------------------
# File name     : led_1.py
# Despription   : Blinking LED with user input
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2017/09/10
#----------------------------------------------------

# Imports
import RPi.GPIO as io
import sys
import time

# define LED Port number
ledPin = 7 # PIn 7 equals GPIO 7

try:
    # user input how often and how long LED should blink
    counter = int(input("How often should LED blink?"))
    lightTime = int(input("And how long in seconds?"))

    #use GPIO PIN-Numbers
    io.setmode(io.BOARD)
    io.setup(ledPin, io.OUT)

    # Blink for counter times for lightTime seconds
    for x in range (0, counter):
        print ("...led on for " +str(x+1) +" time(-s)")
        io.output(ledPin, io.HIGH) # led on
        time.sleep(lightTime) 
        print ("...led off")
        io.output(ledPin, io.LOW) # led off
        time.sleep(lightTime)

except KeyboardInterrupt: # manual exit on Ctrl-C
    print ("Manual user exit occured!")

except: # exception handling
    print ("Some error or exception occured!")
    sys.exc_info()[0]
    raise
finally:
    io.output(ledPin, io.LOW) # led off
    io.cleanup() # release ressource


