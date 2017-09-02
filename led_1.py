#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
#PIN-Nummern verwenden
GPIO.setmode(GPIO.BOARD)
# PIN 7 = GPIO 7
GPIO.setup(7, GPIO.OUT)

# Pin 7 einschalten
GPIO.output(7, GPIO.HIGH)
# 5 Sekunden sleep
time.sleep(5)
GPIO.output(7, GPIO.LOW)

# wieder freigeben
GPIO.cleanup()


