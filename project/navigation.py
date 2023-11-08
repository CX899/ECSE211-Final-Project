import supressants_roulette as sr
import movement as move
import line_tracking as lt
import color_processing


color_centers = color_processing.train_model()
sr.init_all()

cur_location = [0, 0]
facing = 0 # Facing in pos x is 0, pos y is 1, neg x 2, neg y 3
locations = []
colors = ["red", "green", "yellow", "purple", "orange", "blue"]
for i in range(3):
    x = "a"
    while not (x.isdigit() and int(x) >= 0 and int(x) < 4):
        x = input(f"X-Coordinate {i + 1}: ")
    x = int(x)
    y = "a"
    while not (y.isdigit() and int(y) >= 0 and int(y) < 4):
        y = input(f"Y-Coordinate {i + 1}: ")
    y = int(x)
    color = ""
    while not color in colors:
        color = input("Fire color: ")
    locations.append([x, y, color])
try:
    while len(locations) > 0:
        destination = locations[0]

        if cur_location[0] < destination[0]:
            if facing == 1:
                move.turn_90()
            elif facing == 2:
                move.turn_180()
            elif facing == 3:
                move.turn_90(False)
            facing = 0
        elif cur_location[0] > destination[0]:
            if facing == 1:
                move.turn_90(False)
            elif facing == 3:
                move.turn_90()
            elif facing == 0:
                move.turn_180()
            facing = 2
        
        while cur_location[0] != destination[0]:
            move.increment_forward()
            lt.track_line(color_centers)
            if facing == 0:
                cur_location[0] += 1
            else:
                cur_location[0] -= 1
            move.align_turn()

        if cur_location[1] < destination[1]:
            if facing == 0:
                move.turn_90(False)
            elif facing == 2:
                move.turn_90()
            elif facing == 3:
                move.turn_180()
            facing = 1
        elif cur_location[1] > destination[1]:
            if facing == 0:
                move.turn_90()
            elif facing == 1:
                move.turn_180()
            elif facing == 2:
                move.turn_90(False)
            facing = 3
        
        while cur_location[1] != destination[1]:
            move.increment_forward()
            lt.track_line(color_centers)
            if facing == 1:
                cur_location[1] += 1
            else:
                cur_location[1] -= 1
            move.align_turn()
        
        sr.reset_carousel()
        sr.select_block(colors.index(destination[2]))

        locations.pop(0)

    move.stop()
    sr.kill()

except BaseException():
    move.stop()
    sr.kill()