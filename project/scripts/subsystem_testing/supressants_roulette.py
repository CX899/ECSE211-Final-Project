#!/usr/bin/env python3

from utils.brick import BP, wait_ready_sensors, Motor, reset_brick
import time
import line_tracking


#### SETUP ####
CAROUSSEL_MOTOR = Motor("A")
LEVER_MOTOR = Motor("B")
motor_speed = 50
MOTOR_POLL_SLEEP = 0.05
POWER_LIMIT = 100
SPEED_LIMIT = 720

#### FUNCTIONS ####
def wait_for_motor(motor: Motor):
    while BP.get_motor_status(motor.port)[3] == 0:
        time.sleep(MOTOR_POLL_SLEEP)
    while BP.get_motor_status(motor.port)[3] != 0:
        time.sleep(MOTOR_POLL_SLEEP)
    
def init_motor(motor: Motor):
    try:
        motor.reset_encoder()
        motor.set_limits(power=POWER_LIMIT, speed=SPEED_LIMIT)
        motor.set_power(0)
    except IOError as error:
        print(error)


def select_block(supressant_blocks_delivered):
    """
    Drops the correct fire_suppresant based on the total number of fire_suppresants already delivered.

    Params
    ------
        supressant_blocks_delivered: int
            The total number of fire_suppresants already delivered

    Returns
    -------
        None
    """
    if supressant_blocks_delivered == 0:
        BP.set_motor_position(BP.PORT_B, 360)
    elif supressant_blocks_delivered == 1:
        BP.set_motor_position(BP.PORT_A, 60)
        BP.set_motor_position(BP.PORT_B, 360)
    else:
        BP.set_motor_position(BP.PORT_A, 60)
        BP.set_motor_position(BP.PORT_B, 360)
    
    return None

#### MAIN LOOP ####
if __name__ == '__main__':
    wait_ready_sensors()
    supressant_blocks_delivered = 0
    try:
        while True:
            ##select_block(supressant_blocks_delivered)
            ##supressant_blocks_delivered += 1
            BP.set_motor_position(BP.PORT_B, 360)
            wait_for_motor(LEVER_MOTOR)
            BP.set_motor_position(BP.PORT_A, 60)
            wait_for_motor(CAROUSSEL_MOTOR)
            BP.set_motor_position(BP.PORT_B, 360)
            wait_for_motor(LEVER_MOTOR)
    except KeyboardInterrupt:
        kill()
        
                