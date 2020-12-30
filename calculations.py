"""
A program to calculate the number of steps required to lower the blinds
"""
import math

totalSteps = 0  # Number of steps required for the stepper motor to turn
distance = 100  # Distance for the blind cord to be moved (recorded as centimeters)
diameter = 2.8  # Diameter of stepper motor gear (recorded as centimeters)
pi = math.pi
degreeStep = 1.8 / 32


def calculate():
    """
    A function to work out the esimated number of steps for the motor to turn

    :return the calculated steps
    """
    global totalSteps
    circumGear = pi * diameter  # Works out the circumference of the stepper motor gear
    stepsTurn = 360 / degreeStep  # Works out how many steps are required for a full rotation
    gearTurn = distance / circumGear  # Works out number of rotations by the gear

    totalSteps = gearTurn * stepsTurn  # Works out the number of steps required
    stepsRequired = 50000 # Counted from tests of required tests --> Look at logs of recent movement
    return stepsRequired
