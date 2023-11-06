#!/usr/bin/env python3

"""
This code is used to detect the color of the line and output the data to the different subsystems.
"""
from color_processing import classify
from utils.brick import EV3ColorSensor, wait_ready_sensors, Motor
from time import sleep

#### GLOBAL VARIABLES ####

COLOR_SENSOR = EV3ColorSensor(...)
SENSOR_POLL_SLEEP = 0.05

LEFT_MOTOR = Motor("A")
RIGHT_MOTOR = Motor("B") 

LT_HIGH_POWER = 20
LT_LOW_POWER = 18

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.

def track_line(color, model):
    """
    Runs an infinite loop to follow a colored line until a green block is reached. 
    Does so by driving at a very slight angle until the line is no longer in sight, then switching direction,
    and repeating.

    Params
    ------
        color : int
            The color of the line in question - 0 for blue, 1 for red
        model : Model
            The model with which to classify colors
    
    Returns
    -------
        None
    """
    color_detected = color
    LEFT_MOTOR.set_power(LT_HIGH_POWER)
    RIGHT_MOTOR.set_power(LT_LOW_POWER)
    while color_detected != 2:
        sleep(SENSOR_POLL_SLEEP)
        color_detected = classify(COLOR_SENSOR.get_value(), model)
        if color_detected != color:
            if LEFT_MOTOR.get_power() == LT_HIGH_POWER:
                LEFT_MOTOR.set_power(LT_LOW_POWER)
                RIGHT_MOTOR.set_power(LT_HIGH_POWER)
            else:
                LEFT_MOTOR.set_power(LT_HIGH_POWER)
                RIGHT_MOTOR.set_power(LT_LOW_POWER)
    LEFT_MOTOR.set_power(0)
    RIGHT_MOTOR.set_power(0)


def determine_color():
    """

    params
    ------
    None

    returns
    -------
    None
    """
    try:
        while True: # Infinite loop
            data = COLOR_SENSOR.get_value() # Reads color sensor if conditions are met
            return data
    except BaseException(): # Catches all exceptions including KeyboardInterrupt
        exit()


if __name__ == "__main__":
    determine_color()