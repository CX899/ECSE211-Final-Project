#!/usr/bin/env python3

"""
This code is used to detect the color of the line and output the data to the different subsystems.
"""
import color_processing
from utils.brick import EV3ColorSensor, wait_ready_sensors, Motor
from time import sleep

#### GLOBAL VARIABLES ####

COLOR_SENSOR_1 = EV3ColorSensor(1)
COLOR_SENSOR_2 = EV3ColorSensor(2)
SENSOR_POLL_SLEEP = 0.05

LEFT_MOTOR = Motor("D")
RIGHT_MOTOR = Motor("C") 

LT_HIGH_POWER = -20
LT_LOW_POWER = -10

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.

def track_line(color_centers):
    """
    Runs an infinite loop to follow a colored line until a green block is reached. 
    Does so by driving at a very slight angle until the line is no longer in sight, then switching direction,
    and repeating.

    Params
    ------
        model : Model
            The model with which to classify colors
    
    Returns
    -------
        None
    """
    point_left = COLOR_SENSOR_1.get_value()
    point_right = COLOR_SENSOR_2.get_value()
    color_left = color_processing.classify(point_left, color_centers)
    color_right = color_processing.classify(point_right, color_centers)
    
    while color_left != 2 and color_right != 2:
        if color_right != 3: # Note: inverted due to hardware error
            LEFT_MOTOR.set_power(LT_LOW_POWER)
            RIGHT_MOTOR.set_power(LT_HIGH_POWER)
        elif color_left != 3:
            LEFT_MOTOR.set_power(LT_HIGH_POWER)
            RIGHT_MOTOR.set_power(LT_LOW_POWER)
        else:
            LEFT_MOTOR.set_power(LT_HIGH_POWER)
            RIGHT_MOTOR.set_power(LT_HIGH_POWER)

        sleep(SENSOR_POLL_SLEEP)
        point_left = COLOR_SENSOR_1.get_value()
        point_right = COLOR_SENSOR_2.get_value()
        color_left = color_processing.classify(point_left, color_centers)
        color_right = color_processing.classify(point_right, color_centers)

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
            data = COLOR_SENSOR_1.get_value() # Reads color sensor if conditions are met
            return data
    except BaseException(): # Catches all exceptions including KeyboardInterrupt
        exit()


if __name__ == "__main__":
    color_centers = color_processing.train_model()
    track = "y"
    while track == "y":
        track_line(color_centers)
        track = input("Enter y to go again, anything else to stop: ").lower()