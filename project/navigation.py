cur_location = [0, 0]
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