#!/usr/bin/env python3

from utils.brick import BP, wait_ready_sensors, Motor, reset_brick
import time
import line_tracking

#### SETUP ####
CAROUSSEL_MOTOR = Motor("A")
LEVER_MOTOR = Motor("B")
MOTOR_SPEED = 50
MOTOR_POLL_SLEEP = 0.05
POWER_LIMIT = 100
SPEED_LIMIT = 720

#### FUNCTIONS ####
def kill():
    """
    Kills all sound and motion and stops the program.
    """
    CAROUSSEL_MOTOR.set_power(0) # Stop motors
    LEVER_MOTOR.set_power(0) # Stop motors
    BP.reset_all()
    exit()

def wait_for_motor(motor: Motor):
    while BP.get_motor_status(motor.port)[3] == 0:
        time.sleep(MOTOR_POLL_SLEEP)
    while BP.get_motor_status(motor.port)[3] != 0:
        time.sleep(MOTOR_POLL_SLEEP)
    
def init_motor(motor: Motor):
    try:
        motor.set_position(0)
        motor.set_limits(power=POWER_LIMIT, speed=SPEED_LIMIT)
        motor.set_power(0)
    except IOError as error:
        print(error)


def select_block(color_to_select):
    """
    Drops the correct fire_suppresant based on the total number of fire_suppresants already delivered.

    Params
    ------
        color_to_select: int
            The color of the fire suppressant to be dropped. 0 for red, 1 for green, 2 for yellow, 3
            for purple, 4 for orange, 5 for blue

    Returns
    -------
        None
    """
    # Boot in red suppressant
    if color_to_select == 0:
        LEVER_MOTOR.set_position_relative(-360)
        wait_for_motor(LEVER_MOTOR)
    # Boot in green suppressant    
    elif color_to_select == 1:
        CAROUSSEL_MOTOR.set_position_relative(60)
        wait_for_motor(CAROUSSEL_MOTOR)
        LEVER_MOTOR.set_position_relative(-360)
    # Boot in yellow suppressant
    elif color_to_select == 2:
        CAROUSSEL_MOTOR.set_position_relative(120)
        wait_for_motor(CAROUSSEL_MOTOR)
        LEVER_MOTOR.set_position_relative(-360)
    # Boot in purple suppressant
    elif color_to_select == 3:
        CAROUSSEL_MOTOR.set_position_relative(180)
        wait_for_motor(CAROUSSEL_MOTOR)
        LEVER_MOTOR.set_position_relative(-360)
    # Boot in orange suppressant
    elif color_to_select == 4:
        CAROUSSEL_MOTOR.set_position_relative(-120)
        wait_for_motor(CAROUSSEL_MOTOR)
        LEVER_MOTOR.set_position_relative(-360)
    # Boot in blue suppressant
    else:
        CAROUSSEL_MOTOR.set_position_relative(-60)
        wait_for_motor(CAROUSSEL_MOTOR)
        LEVER_MOTOR.set_position_relative(-360)

    return None

def reset_carousel():
    # Resets carousel and lever to 0 position.
    CAROUSSEL_MOTOR.set_position(0)
    wait_for_motor(CAROUSSEL_MOTOR)
    LEVER_MOTOR.set_position(0)
    wait_for_motor(LEVER_MOTOR)

def init_all():
    init_motor(CAROUSSEL_MOTOR)
    init_motor(LEVER_MOTOR)
    wait_ready_sensors()    

#### MAIN LOOP ####
if __name__ == '__main__':
    init_motor(CAROUSSEL_MOTOR)
    init_motor(LEVER_MOTOR)
    wait_ready_sensors()
    try:
        color_to_select = 0 # Dummy variable
        #color_to_select = line_tracking.determine_color()
        select_block(color_to_select)
    except KeyboardInterrupt:
        kill()
        
                