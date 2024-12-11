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

    elif direction == ">":
        if guard_pos_x + 1 <= lab_map.shape[1] - 1:
            if lab_map[guard_pos_y, guard_pos_x + 1] == "#":
                direction = "v"
                valid_step = False
            else:
                guard_pos_x += 1
        else:
            out_of_bound = True
    
    elif direction == "v":
        if guard_pos_y + 1 <= lab_map.shape[0] - 1:                
            if lab_map[guard_pos_y + 1, guard_pos_x] == "#":
                direction = "<"
                valid_step = False
            else:
                guard_pos_y += 1
        else:
            out_of_bound = True
        
    elif direction == "<":
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
all_locations2 = []

all_locations.append(guard_pos)
total_loops = 0

for i in range(0, 2200000):
    valid_step, out_of_bound, new_location, old_location, direction = check_step(direction, lab_map, guard_pos)
    all_locations.append(new_location)
    lab_map[old_location] = "."
    lab_map[new_location] = direction
    guard_pos = (new_location)

    if out_of_bound:
        break
    
    lab_map2 = np.copy(lab_map)
    direction2 = direction
    guard_pos2 = guard_pos
    match direction2:
        case "^":
            if new_location[0] - 1 < 0:
                break
            lab_map2[(new_location[0] - 1, new_location[1])] = "#"
            obstacle_pos = (new_location[0] - 1, new_location[1])
            check_location = obstacle_pos
        case ">":
            if new_location[1] + 1 > lab_map.shape[1] - 1:
                break
            lab_map2[(new_location[0], new_location[1] + 1)] = "#"
            obstacle_pos = (new_location[0], new_location[1] + 1)
            check_location = obstacle_pos
        case "v":
            if new_location[0] + 1 > lab_map.shape[0] - 1:
                break
            lab_map2[(new_location[0] + 1, new_location[1])] = "#"
            obstacle_pos = (new_location[0] + 1, new_location[1])
            check_location = obstacle_pos
        case "<":
            if new_location[1] - 1 < 0:
                break
            lab_map2[(new_location[0], new_location[1] - 1)] = "#"
            obstacle_pos = (new_location[0], new_location[1] - 1)
            check_location = obstacle_pos
    
    lab_map3 = lab_map2
    side_loop_check = True
    
    for step in range(0, 200*200):
        valid_step, out_of_bound2, new_location, old_location, direction2 = check_step(direction2, lab_map2, guard_pos2)
        if valid_step is True and out_of_bound2 is False:
            lab_map2[new_location] = direction2
            lab_map2[old_location] = "."
            guard_pos2 = (new_location)

        if out_of_bound2:
            side_loop_check = False
            break
    if side_loop_check is True:
        if check_location not in all_locations:
            total_loops += 1
            all_locations2.append(obstacle_pos)

print(total_loops)
all_locations = set(all_locations)
print(len(all_locations))
all_locations2 = set(all_locations2)
print(len(all_locations2))