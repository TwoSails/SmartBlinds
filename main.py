import RPi.GPIO as GPIO
from motor import Motor
from time import sleep
import time
import calculations
from logData import *
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

powerBtn = 18
switch = 4
shutdown = False
count = 0

steps = calculations.calculate()
motor = Motor(steps)
state = loadLog()

motor.setup()

GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(powerBtn, GPIO.IN, GPIO.PUD_UP)

while not shutdown:
    power_state = GPIO.input(powerBtn)
    relay_state = GPIO.input(switch)
    if power_state == GPIO.LOW:
        print('Shutting down...')
        motor.cleanup()
        shutdownLog(state)
        sleep(2)
        os.system('sudo shutdown -H now')

    elif relay_state == GPIO.LOW:
        print('Activate')

        if state == "open" or state == 'open - paused':
            timeStart = time.time()
            completed = motor.descend()
            timeEnd = time.time()
            makeData(count, "closed", completed, timeStart, timeEnd)
            state = "closed"

        elif state == "closed":
            timeStart = time.time()
            completed = motor.ascend()
            timeEnd = time.time()
            makeData(count, "open", completed, timeStart, timeEnd)
            state = "open"

        elif state == 'paused':
            timeStart = time.time()
            completed = motor.descend()
            timeEnd = time.time()
            makeData(None, "closed-after pause", completed, timeStart, timeEnd)
            state = 'open - paused'

        else:
            print('Error >> Unknown state')

    else:
        pass
#        print('Error >> Something has gone wrong')
