import numpy as np

loc = "data/d6.txt"

lab_map = []

with open(loc) as f:
    for line in f:
        tile_map = [tile for tile in line.replace("\n", "")]
        lab_map.append(tile_map)

lab_map = np.array(lab_map)

guard_pos = np.where(lab_map == "^")
guard_pos_y = guard_pos[0][0]
guard_pos_x = guard_pos[1][0]
guard_pos = (guard_pos_y, guard_pos_x)

direction = "^"

def check_step(direction, lab_map, guard_pos):
    valid_step = True
    out_of_bound = False
    guard_pos_y = guard_pos[0]
    guard_pos_x = guard_pos[1]
    old_location = guard_pos
    if direction == "^":
        if guard_pos_y - 1 >= 0:
            if lab_map[guard_pos_y - 1, guard_pos_x] == "#":
                direction = ">"
                valid_step = False
            else:
                guard_pos_y -= 1
        else:
            out_of_bound = True

    if direction == ">":
        if guard_pos_x + 1 <= lab_map.shape[1] - 1:
            if lab_map[guard_pos_y, guard_pos_x + 1] == "#":
                direction = "v"
                valid_step = False
            else:
                guard_pos_x += 1
        else:
            out_of_bound = True
    
    if direction == "v":
        if guard_pos_y + 1 <= lab_map.shape[0] - 1:                
            if lab_map[guard_pos_y + 1, guard_pos_x] == "#":
                direction = "<"
                valid_step = False
            else:
                guard_pos_y += 1
        else:
            out_of_bound = True
        
    if direction == "<":
        if guard_pos_x - 1 >= 0:
            if lab_map[guard_pos_y, guard_pos_x - 1] == "#":
                direction = "^"
                valid_step = False
            else:
                guard_pos_x -= 1
        else:
            out_of_bound = True

    new_location = (guard_pos_y, guard_pos_x)
    return valid_step, out_of_bound, new_location, old_location, direction

all_locations = []

all_locations.append(guard_pos)

for i in range(0, 211111111111111111111110):
    valid_step, out_of_bound, new_location, old_location, direction = check_step(direction, lab_map, guard_pos)

    if valid_step is True and out_of_bound is False:
        lab_map[new_location] = direction
        all_locations.append(new_location)
        lab_map[old_location] = "."
        guard_pos = (new_location)

    if out_of_bound:
        break

print(all_locations)
all_locations = set(all_locations)
print(len(all_locations))