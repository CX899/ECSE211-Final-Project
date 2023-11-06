import supressants_roulette as sr
import movement as move
import line_tracking as lt

cur_location = [0, 0]
facing = 0 # Facing in pos x is 0, pos y is 1, neg x 2, neg y 3
locations = []
for i in range(3):
    x = "a"
    while not (x.isdigit() and int(x) >= 0 and int(x) < 4):
        x = input(f"X-Coordinate {i + 1}: ")
    x = int(x)
    y = "a"
    while not (y.isdigit() and int(y) >= 0 and int(y) < 4):
        y = input(f"Y-Coordinate {i + 1}: ")
    y = int(x)
    locations.append([x, y])

while len(locations) > 0:
    destination = locations[0]

    if destination[0] < locations[0]:
        if facing == 1:
            move.turn_90()
        elif facing == 2:
            move.turn_180()
        elif facing == 3:
            move.turn_90(False)
        facing = 0
    elif destination[0] > locations[0]:
        if facing == 1:
            move.turn_90(False)
        elif facing == 3:
            move.turn_90()
        elif facing == 0:
            move.turn_180()
        facing = 2

    while cur_location[0] != destination[0]:
        lt.track_line(0)
        cur_location[0] += 1
        move.align_turn()

sr.kill()