#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

#use GPIO PIN-Numbers
GPIO.setmode(GPIO.BOARD)

# PIN 7 equals GPIO 7
GPIO.setup(7, GPIO.OUT)

# Set PIN 7
GPIO.output(7, GPIO.HIGH)

# Blink for 5 times for 3 seconds
for x in range (0, 5):
   time.sleep(3) 
   GPIO.output(7, GPIO.LOW)
   time.sleep(3)
   GPIO.output(7, GPIO.HIGH)

# reset PIN
GPIO.cleanup()


