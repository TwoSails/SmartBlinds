import RPi.GPIO as GPIO
from time import *


class Motor:
    def __init__(self, steps):
        self.delay = 0.0001  # Sets the delay between pulses - Basically controls the speed of the motor
        self.PUL = 17  # Stepper Drive Pin
        self.DIR = 27  # Direction Control Bit (HIGH for Controller default / LOW to Force a Direction Change)
        self.ENA = 22  # Enable Control Bit (HIGH for Enable / LOW for Disable)
        self.downSwitch = 6
        self.upSwitch = 5
        self.relay = 4
        self.cycles = steps

    def setup(self):
        GPIO.setmode(GPIO.BCM)  # Sets the mode for the GPIO Pins - NOTE: It will not work if it is in GPIO.BOARD

        GPIO.setup(self.PUL, GPIO.OUT)  # Sets up the pin for the Stepper Drive Pulse
        GPIO.setup(self.DIR, GPIO.OUT)  # Sets up the pin for the Directional Bit
        GPIO.setup(self.ENA, GPIO.OUT)  # Sets up the pin for the Enable Bit
        GPIO.setup(self.downSwitch, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.upSwitch, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.relay, GPIO.IN, GPIO.PUD_UP)

    def descend(self):

        print('Motor - descending')
        steps = 0

        GPIO.output(self.ENA, GPIO.HIGH)  # Enables the Stepper Driver
        sleep(.5)  # Allows for any updates
        GPIO.output(self.DIR, GPIO.LOW)  # Sets the direction of the motor


        while steps <= self.cycles:  # Pulses the motor for the length of the blinds
            relay_state = GPIO.input(self.relay)
            downStateSwitch = GPIO.input(self.downSwitch)

            GPIO.output(self.PUL, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.PUL, GPIO.LOW)
            sleep(self.delay)
            steps += 1
            if downStateSwitch == GPIO.LOW or relay_state == GPIO.LOW:
                print('downSwitch')
                GPIO.output(self.ENA, GPIO.LOW)
                break

        GPIO.output(self.ENA, GPIO.LOW)  # Disables the Stepper Driver

        sleep(.5)  # Allows for any updates

        return steps

    def ascend(self):
        print('Motor - ascending')
        steps = 0

        GPIO.output(self.ENA, GPIO.HIGH)  # Enables the Stepper Driver
        sleep(.5)  # Allows for any updates
        GPIO.output(self.DIR, GPIO.HIGH)  # Sets the direction of the motor

        while steps <= self.cycles:  # Pulses the motor for the length of the blinds
            relay_state = GPIO.input(self.relay)
            upStateSwitch = GPIO.input(self.upSwitch)

            GPIO.output(self.PUL, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.PUL, GPIO.LOW)
            sleep(self.delay)
            steps += 1
            if upStateSwitch == GPIO.LOW or relay_state == GPIO.LOW:
                print('Motor - downSwitch activated')
                GPIO.output(self.ENA, GPIO.LOW)
                break

        GPIO.output(self.ENA, GPIO.LOW)  # Disables the Stepper Driver

        sleep(.5)  # Allows for any updates

        return steps

    def cleanup(self):
        GPIO.cleanup()  # Cleans up the pins on the board
        print('Motor - Cleaning Up GPIO')
