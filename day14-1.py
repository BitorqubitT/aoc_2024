import numpy as np

loc = "data/d14.txt"

def time_step(robots):
    new_robots = []
    for i in robots:
        velocity = i[0]
        pos = i[1]
        new_pos_x = pos[0] + velocity[0]
        new_pos_y = pos[1] + velocity[1]
        if new_pos_x < 0:
            new_pos_x = bathroom.shape[1] + new_pos_x
        if new_pos_x >= bathroom.shape[1]:
            new_pos_x = new_pos_x - bathroom.shape[1]
        if new_pos_y < 0:
            new_pos_y = bathroom.shape[0] + new_pos_y
        if new_pos_y >= bathroom.shape[0]:
            new_pos_y = new_pos_y - bathroom.shape[0]
        new_robots.append([velocity, [new_pos_x, new_pos_y]])
    return new_robots

def split_matrix(matrix):
    rows, cols = matrix.shape

    mid_row = rows // 2
    mid_col = cols // 2

    matrix = np.delete(matrix, mid_row, axis=0)
    matrix = np.delete(matrix, mid_col, axis=1)

    top_left = matrix[:mid_row, :mid_col]
    top_right = matrix[:mid_row, mid_col:]
    bottom_left = matrix[mid_row:, :mid_col]
    bottom_right = matrix[mid_row:, mid_col:]

    return top_left, top_right, bottom_left, bottom_right

robots = []

with open(loc, "r") as f:
    for line in f:
        robot_stats = []
        velocity = line.split()[0].replace('p=',"").split(",")
        pos = line.split()[1].replace("v=","").split(",")
        pos = [int(x) for x in pos]
        velocity = [int(x) for x in velocity]
        robots.append([pos, velocity])

bathroom = np.zeros((103, 101))

for i in range(0, 100):
    robots = time_step(robots)

for i in robots:
    pos = i[1]
    bathroom[pos[1], pos[0]] = bathroom[pos[1], pos[0]] + 1

# Example usage
top_left, top_right, bottom_left, bottom_right = split_matrix(bathroom)
all_parts = split_matrix(bathroom)

total = 1 
for part in all_parts:
    total *= np.sum(part)

print(total)