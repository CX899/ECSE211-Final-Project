from utils.brick import Motor, BP, EV3GyroSensor, wait_ready_sensors
import math, time
import color_processing
import line_tracking

#### GLOBAL VARIABLES ####
# Note: these variables are temporary and subject to change upon hardware completion

LEFT_MOTOR = Motor("D")
RIGHT_MOTOR = Motor("C") 
GYRO_SENSOR = EV3GyroSensor(3)
MOTOR_SEPERATION = 8.5 # Functionally the width of the robot, used for calculating turns
WHEEL_RADIUS = 2.15
COLOR_SENSOR_OFFSET = 10 # Distance from color sensor to motors, used to realign sensor for turns
MOTOR_SPEED = 20
MOTOR_POLL_SLEEP = 0.05
POWER_LIMIT = 75
SPEED_LIMIT = 100
FORWARD_INCREMENT = 5

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
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT)
        motor.set_power(0)
        time.sleep(1)
    except IOError as error:
        print(error)

def increment_forward():
    """ Aligns drop chute to the green square. 
    """
    angle = -180 * FORWARD_INCREMENT / math.pi / WHEEL_RADIUS
    LEFT_MOTOR.set_position_relative(angle)
    RIGHT_MOTOR.set_position_relative(angle)
    wait_for_motor(RIGHT_MOTOR)

def align_turn():
    """ Rolls robot forward to center green square between the motors before turning,
    so as to align the color sensor with the perpendicular line when the turn is complete.
    """
    angle = -180 * COLOR_SENSOR_OFFSET / math.pi / WHEEL_RADIUS
    LEFT_MOTOR.set_position_relative(angle)
    RIGHT_MOTOR.set_position_relative(angle)
    wait_for_motor(RIGHT_MOTOR)

def turn_90():
    wait_ready_sensors()
    
    current_angle = GYRO_SENSOR.get_abs_measure()
    target_angle = current_angle + 90
    
    print(current_angle)
    print(target_angle)
            
    
    LEFT_MOTOR.set_power(-15)
    RIGHT_MOTOR.set_power(15)

    while True:
        if current_angle < target_angle:
            current_angle = GYRO_SENSOR.get_abs_measure()
            time.sleep(0.02)  # Small delay to prevent excessive sensor polling
            print(abs(current_angle))
            print(target_angle)
            print("Turning")
        else:
            print("done")
            break

    # Stop motors
    LEFT_MOTOR.set_power(0)
    RIGHT_MOTOR.set_power(0)

if __name__ == '__main__':
    init_motor(LEFT_MOTOR)
    init_motor(RIGHT_MOTOR)
    GYRO_SENSOR.reset_measure()
    time.sleep(0.1)
    # color_centers = color_processing.train_model()

    # track = "y"
    # while track == "y":
    #     line_tracking.track_line(color_centers)
    #     init_motor(LEFT_MOTOR)
    #     init_motor(RIGHT_MOTOR)
    #     align_turn
    #     track = input("Enter y to go again, anything else to stop: ").lower()
    
    turn_90()