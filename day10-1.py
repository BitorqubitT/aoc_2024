import numpy as np
loc = "data/d10.txt"

lava_map = []

with open(loc) as f:
    for line in f:
        line.replace("\n", "")
        tile_map = [int(tile) for tile in line.replace("\n", "")]
        lava_map.append(tile_map)

lava_map = np.array(lava_map)

print(lava_map)
start_positions = []
start_position = np.where(lava_map == 0)
for x, y in zip(start_position[0], start_position[1]):
    start_positions.append((x, y))

def find_next_positions(height, locations):
    if height == 0:
        locations = [locations]
    new_locations = []
    new_height = height + 1
    if new_height == 10:
        return locations
    for position in locations:
        all_surrounding = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for surrounding_tile in all_surrounding:
            new_y = position[0] + surrounding_tile[0]
            new_x = position[1] + surrounding_tile[1]
            if (new_y >= 0 and new_y < lava_map.shape[0]) and (new_x >= 0 and new_x < lava_map.shape[1]):
                if lava_map[new_y, new_x] == new_height:
                        new_locations.append((new_y, new_x))
    locations = find_next_positions(new_height, new_locations)
    return locations
    
total = 0
for i in start_positions:
    total += len(set(find_next_positions(0, i)))

print(total)