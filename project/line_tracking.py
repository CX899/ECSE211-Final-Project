#!/usr/bin/env python3

"""
This code is used to detect the color of the line and output the data to the different subsystems.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors


# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(...)
SENSOR_POLL_SLEEP = 0.05

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


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