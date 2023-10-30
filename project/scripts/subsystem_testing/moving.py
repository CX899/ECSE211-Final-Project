#!/usr/bin/env python3

from utils.brick import BP, wait_ready_sensors, Motor, reset_brick
import time
import line_tracking


#### SETUP ####
RIGHT_MOTOR = Motor("A")
LEFT_MOTOR = Motor("A")
motor_speed = 50
SENSOR_POLL_SLEEP = 0.05

#### FUNCTIONS ####


def select_movement():
    """
    
    """
    pass

#### MAIN LOOP ####
if __name__ == '__main__':
    wait_ready_sensors()
    try:
        while True:
            pass
            
    except KeyboardInterrupt:
        kill()
        
                