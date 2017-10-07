#!/usr/bin/python3

#----------------------------------------------------
# File name     : temp_sens_1.py
# Despription   : Read temperature sensor DS18B20 data 
#                 and plot on screen
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2017/10/07
#----------------------------------------------------

# Imports
import os
import glob
import sys
import time

# Enable Sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Set directory and file
base_dir = '/sys/bus/w1/devices/'

if len(glob.glob(base_dir + '28*')) > 0:
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
else:
    sys.exit('No sensor connected')

# Read raw temperature data
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

# Read temperature as celsius
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Plot temperature every x seconds
try:
    while True:
        print(read_temp())
        time.sleep(5)

except KeyboardInterrupt: # manual exit on Ctrl-C
    print ("Manual user exit occured!")
