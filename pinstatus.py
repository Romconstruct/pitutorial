#!/usr/bin/python3

# Small script to check state of a GPIO pin

# Imports
import RPi.GPIO as io
import sys

try:
    # let user specify a pin
    pin = int(input("Specifiy a PIN Number"))

    io.setmode(io.BOARD)
    io.setup(pin, io.IN)

    # read pin state
    state = io.input(pin)
    
    # output
    if (state is True):
        print("PIN", pin ,"state is high")
    else:
        print("PIN", pin ,"state is low")

except:
    # Exception output
    print("Some error or exception occured!")
    sys.exc_info()[0]
    raise

finally:
    # reset PIN
    io.cleanup()

