#!/usr/bin/python3

# small LED blinking script with GPIO Board
# script assumes fix GPIO port 7 is usec

import RPi.GPIO as io
import sys
import time

try:
    # user input how often and how long LED should blink
    counter = int(input("How often should LED blink?"))
    lightTime = int(input("And how long in seconds?"))

    #use GPIO PIN-Numbers
    io.setmode(io.BOARD)

    # PIN 7 equals GPIO 7
    io.setup(7, io.OUT)

    # Blink for 5 times for 3 seconds
    for x in range (0, counter):
        io.output(7, 1) 
        time.sleep(lightTime) 
        io.output(7, 0)
        time.sleep(lightTime)

except KeyboardInterrupt:
    # CTRL-C exit
    print ("Manual user exit occured!")

except:
    # exception output
    print ("Some error or exception occured!")
    sys.exc_info()[0]
    raise
finally:
    # reset PIN
    io.cleanup()


