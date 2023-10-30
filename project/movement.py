from utils.brick import Motor
import math

#### GLOBAL VARIABLES ####
# Note: these variables are temporary and subject to change upon hardware completion

left = Motor("A")
right = Motor("B") 
motor_separation = 40 # Functionally the width of the robot, used for calculating turns
wheel_radius = 5 
color_sensor_offset = 20 # Distance from color sensor to motors, used to realign sensor for turns

def turn_90(turn_cw=True):
    """ Rotates robot 90 degrees from current position. 

    Params
    ------
        turn_cw : boolean
            True if turning clockwise, False otherwise
    """
    angle = 45 * motor_separation / wheel_radius
    
    if turn_cw:
        left.set_position_relative(angle)
        right.set_position_relative(-angle)
    else:
        left.set_position_relative(-angle)
        right.set_position_relative(angle)


def turn_180():
    for i in range(2):
        turn_90()

def align_turn():
    """ Rolls robot forward to center green square between the motors before turning,
    so as to align the color sensor with the perpendicular line when the turn is complete.
    """
    angle = 180 * color_sensor_offset / math.pi / wheel_radius
    left.set_position_relative(angle)
    right.set_position_relative(angle)