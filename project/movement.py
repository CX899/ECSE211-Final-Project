from utils.brick import Motor

#### GLOBAL VARIABLES ####
# Note: these variables are temporary and subject to change upon hardware completion

left = Motor("A")
right = Motor("B") 
motor_separation = 40 # Functionally the width of the robot, used for calculating turns
wheel_radius = 5 

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