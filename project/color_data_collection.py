from utils.brick import EV3ColorSensor
from time import sleep

CS = EV3ColorSensor(1)
SENSOR_POLL_SLEEP = 0.05

if __name__ == "__main__":
    colors = ["blue", "green", "red"]
    for color in colors:
        input(f"Press enter to start collecting {color}")
        print(f"COLLECTING {color.upper()}")
        try:
            f = open(f"./color_data/{color}.csv")
            for i in range(100):
                data = CS.get_value()
                f.write(f"{data}\n")
                sleep(SENSOR_POLL_SLEEP)
            f.close()
        except BaseException():
            f.close()
            exit()
