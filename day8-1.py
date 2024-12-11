import numpy as np
import math

loc = "data/d8.txt"

lab_map = []

with open(loc) as f:
    for line in f:
        tile_map = [tile for tile in line.replace("\n", "")]
        lab_map.append(tile_map)

all_unique = set([j for i in lab_map for j in i])
all_unique.remove(".")
lab_map = np.array(lab_map)
all_locations = []
for antenna_sign in all_unique:
    location_per_antenna_type = []

    antenna_position = np.where(lab_map == antenna_sign)
    for x, y in zip(antenna_position[0], antenna_position[1]):
        location_per_antenna_type.append((x, y))
    all_locations.append(location_per_antenna_type)

def calc_angle(point1, point2):
    delta_y = point1[0] - point2[0]
    delta_x = point1[1] - point2[1]
    angle = math.atan2(delta_y, delta_x)
    angle_degrees = math.degrees(angle)
    return angle_degrees

def calc_signal_pos(angle, distance, starting_point):
    # numpy x,y is diff
    x = starting_point[1] + (distance*2) * math.cos(math.radians(angle))
    y = starting_point[0] + (distance*2) * math.sin(math.radians(angle))
    print(x,y)
    return (int(round(y)), int(round(x)))

all_signal_positions = []

for antenna_type in all_locations:
    for antenna_pos in antenna_type:
        for other_antenna_pos in  antenna_type:
            if antenna_pos == other_antenna_pos:
                continue
            else:
                distance = np.sqrt((other_antenna_pos[0] - antenna_pos[0])**2 + (other_antenna_pos[1] - antenna_pos[1])**2)
                angle = calc_angle(other_antenna_pos, antenna_pos)
                signal_pos = calc_signal_pos(angle, distance, antenna_pos)
                if (signal_pos[0] >= 0 and signal_pos[0] <= lab_map.shape[0] - 1) and (signal_pos[1] >= 0 and signal_pos[1] <= lab_map.shape[1] - 1):
                    print("add these", signal_pos)
                    if signal_pos == (1, 4) or signal_pos == (1, 3):
                        print(antenna_pos, other_antenna_pos, distance, angle)
                    all_signal_positions.append(signal_pos)

for i in all_signal_positions:
    lab_map[i[0], i[1]] = "#"

print(len(set(all_signal_positions)))
    

