import numpy as np
loc = "data/d12.txt"

def find_garden_plot(start_pos, garden_map, plant_type):
    plot_locations = [start_pos]
    counter = 0
    while counter < 300:
        counter += 1
        temp_plot = []
        for plot in plot_locations:
            neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for dy, dx in neighbors:
                new_y, new_x = plot[0] + dy, plot[1] + dx
                if 0 <= new_y < garden_map.shape[0] and 0 <= new_x < garden_map.shape[1]:
                    if garden_map[new_y, new_x] == plant_type and (new_y, new_x) not in plot_locations and (new_y, new_x) not in temp_plot:
                        temp_plot.append((new_y, new_x))
        plot_locations.extend(temp_plot)
    return plot_locations

def get_sides(region):
    sides = 0
    edge_coord_corners = set()

    for x, y in region:
        for dx, dy in [(0.5, 0.5), (0.5, -0.5), (-0.5, 0.5), (-0.5, -0.5)]:
            edge_coord_corners.add((x + dx, y + dy))

    for x, y in edge_coord_corners:
        pattern = "".join("X" if (x + dx, y + dy) in region else "O" for dx, dy in [(0.5, 0.5), (0.5, -0.5), (-0.5, 0.5), (-0.5, -0.5)])
        if pattern in {"OXXO", "XOOX"}:
            sides += 2
        elif pattern.count("X") == 3 or pattern.count("O") == 3:
            sides += 1

    return sides

def read_garden_map(file_path):
    garden_map = []
    with open(file_path) as f:
        for line in f:
            tile_map = [tile for tile in line.strip()]
            garden_map.append(tile_map)
    return np.array(garden_map)

def calculate_total_score(garden_map):
    all_garden_plots = []
    check_plot = set()
    for y in range(garden_map.shape[0]):
        for x in range(garden_map.shape[1]):
            if (y, x) not in check_plot:
                found_plot = find_garden_plot((y, x), garden_map, garden_map[y, x])
                all_garden_plots.append(found_plot)
                check_plot.update(found_plot)

    total = 0
    for plot in all_garden_plots:
        area = len(plot)
        fences = get_sides(plot)
        total_plot_score = fences * area
        total += total_plot_score

    return total

# Example usage
garden_map = read_garden_map(loc)
total_score = calculate_total_score(garden_map)
print(total_score)
