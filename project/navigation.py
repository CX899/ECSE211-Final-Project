import supressants_roulette as sr
import movement as move
import line_tracking as lt
import color_processing

def calc_path(blocked, start, target):
    distances = [[100 for i in range(4)] for j in range(4)]
    cur_cells = [target]
    while len(cur_cells) > 0:
        next_cells = []
        for cell in cur_cells:
            adjacent = []
            if cell[0] > 0:
                adjacent.append([cell[0] - 1, cell[1]])
            if cell[0] < 3:
                adjacent.append([cell[0] + 1, cell[1]])
            if cell[1] > 0:
                adjacent.append([cell[0], cell[1] - 1])
            if cell[1] < 3:
                adjacent.append([cell[0], cell[1] + 1])        
            if cell == target:
                distances[cell[0]][cell[1]] = 0
                for a in adjacent:
                    if distances[a[0]][a[1]] == 100:
                        next_cells.append(a)
            elif not blocked[cell[0]][cell[1]]:
                weights = [distances[a[0]][a[1]] for a in adjacent + [cell]]
                distances[cell[0]][cell[1]] = min(weights) + 1
                for a in adjacent:
                    if distances[a[0]][a[1]] == 100:
                        next_cells.append(a)
            else:
                distances[cell[0]][cell[1]] = 200
        cur_cells = next_cells
    path = []
    cell = start
    while cell[0] != target[0] or cell[1] != target[1]:
        adjacent = []
        if cell[0] > 0:
            adjacent.append([cell[0] - 1, cell[1]])
        if cell[0] < 3:
            adjacent.append([cell[0] + 1, cell[1]])
        if cell[1] > 0:
            adjacent.append([cell[0], cell[1] - 1])
        if cell[1] < 3:
            adjacent.append([cell[0], cell[1] + 1]) 
        weights = [distances[a[0]][a[1]] for a in adjacent]
        coord = adjacent[weights.index(min(weights))]
        coord.append("None")
        path.append(coord)
        cell = path[-1]
    path[-1][-1] = target[2]
    return path

color_centers = color_processing.train_model()
sr.init_all()

cur_location = [0, 0]
prev = [0, 0]
blocked = [[False for i in range(4)] for j in range(4)]
facing = 0 # Facing in pos x is 0, pos y is 1, neg x 2, neg y 3
locations = []
colors = ["D", "F", "B", "C", "E", "A"]
fires = input("Enter fire locations and suppressant types: ").split(",")
blocked[int(fires[0])][int(fires[1])] = True
blocked[int(fires[3])][int(fires[4])] = True
blocked[int(fires[6])][int(fires[7])] = True
for i in range(3):
    x = int(fires[i * 3])
    y = int(fires[i * 3 +1])
    color = fires[i * 3 +2]
    locations.extend(calc_path(blocked, prev, [x, y, color]))
    prev = locations[-2]
    blocked[x][y] = True
    locations.append(prev)
locations.extend(calc_path(blocked, prev, [0, 0, "None"]))

"""
colors = ["red", "green", "yellow", "purple", "orange", "blue"]
for i in range(3):
    x = "a"
    while not (x.isdigit() and int(x) >= 0 and int(x) < 4):
        x = input(f"X-Coordinate {i + 1}: ")
    x = int(x)
    y = "a"
    while not (y.isdigit() and int(y) >= 0 and int(y) < 4):
        y = input(f"Y-Coordinate {i + 1}: ")
    y = int(y)
    color = ""
    while not color in colors:
        color = input("Fire color: ")
    locations.extend(calc_path(blocked, prev, [x, y, color]))
    prev = locations[-2]
    blocked[x][y] = True
    locations.append(prev)
locations.extend(calc_path(blocked, prev, [0, 0, "None"]))
"""
color = 0
align = False
while len(locations) > 0:
    destination = locations[0]

    if cur_location[0] < destination[0]:
        if align:
            move.align_turn()
            align = False
        if facing == 1:
            move.turn_90(False)
        elif facing == 2:
            move.turn_180()
        elif facing == 3:
            move.turn_90()
        facing = 0
    elif cur_location[0] > destination[0]:
        if align:
            move.align_turn()
            align = False
        if facing == 1:
            move.turn_90()
        elif facing == 3:
            move.turn_90(False)
        elif facing == 0:
            move.turn_180()
        facing = 2
    
    while cur_location[0] != destination[0]:
        if align:
            move.align_turn()
            align = False
        lt.track_line(color_centers)
        if facing == 0:
            cur_location[0] += 1
        else:
            cur_location[0] -= 1
        align = True
        

    if cur_location[1] < destination[1]:
        if align:
            move.align_turn()
            align = False
        if facing == 0:
            move.turn_90()
        elif facing == 2:
            move.turn_90(False)
        elif facing == 3:
            move.turn_180()
        facing = 1
    elif cur_location[1] > destination[1]:
        if align:
            move.align_turn()
            align = False
        if facing == 0:
            move.turn_90(False)
        elif facing == 1:
            move.turn_180()
        elif facing == 2:
            move.turn_90()
        facing = 3
    
    while cur_location[1] != destination[1]:
        if align:
            move.align_turn()
            align = False
        lt.track_line(color_centers)
        if facing == 1:
            cur_location[1] += 1
        else:
            cur_location[1] -= 1
        align = True

    if destination[2] in colors:
        align = False
        color = colors.index(destination[2])
        move.turn_180()
        if facing == 0:
            facing = 2
        elif facing == 1:
            facing = 3
        elif facing == 2:
            facing = 0
        else:
            facing = 1
        move.increment_forward()
        sr.select_block(color)
    
    locations.pop(0)

move.align_turn()
move.stop()
sr.kill()
