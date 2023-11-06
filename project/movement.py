from utils.brick import Motor, BP
import math, time

#### GLOBAL VARIABLES ####
# Note: these variables are temporary and subject to change upon hardware completion

LEFT_MOTOR = Motor("A")
RIGHT_MOTOR = Motor("B") 
MOTOR_SEPERATION = 40 # Functionally the width of the robot, used for calculating turns
WHEEL_RADIUS = 5 
COLOR_SENSOR_OFFSET = 10 # Distance from color sensor to motors, used to realign sensor for turns
MOTOR_SPEED = 50
MOTOR_POLL_SLEEP = 0.05
POWER_LIMIT = 100
SPEED_LIMIT = 720
FORWARD_INCREMENT = 20

def stop():
    LEFT_MOTOR.set_power(0)
    RIGHT_MOTOR.set_power(0)

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

def turn_90(turn_cw=True):
    """ Rotates robot 90 degrees from current position. 

    Params
    ------
        turn_cw : boolean
            True if turning clockwise, False otherwise
    """
    angle = 45 * MOTOR_SEPERATION / WHEEL_RADIUS
    
    if turn_cw:
        LEFT_MOTOR.set_position_relative(angle)
        RIGHT_MOTOR.set_position_relative(-angle)
    else:
        LEFT_MOTOR.set_position_relative(-angle)
        RIGHT_MOTOR.set_position_relative(angle)


def turn_180():
    for i in range(2):
        turn_90()

def increment_forward():
    angle = 180 * FORWARD_INCREMENT / math.pi / WHEEL_RADIUS
    LEFT_MOTOR.set_position_relative(angle)
    RIGHT_MOTOR.set_position_relative(angle)

def align_turn():
    """ Rolls robot forward to center green square between the motors before turning,
    so as to align the color sensor with the perpendicular line when the turn is complete.
    """
    angle = 180 * COLOR_SENSOR_OFFSET / math.pi / WHEEL_RADIUS
    LEFT_MOTOR.set_position_relative(angle)
    RIGHT_MOTOR.set_position_relative(angle)