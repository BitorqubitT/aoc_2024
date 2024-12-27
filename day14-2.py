import numpy as np
import matplotlib.pyplot as plt
import gc
loc = "data/d14.txt"

"""
Guessed some values to get a range.
Then print to map and inspect.
"""

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

for z in range(0, 10000):
    robots = time_step(robots)
    bathroom = np.zeros((103, 101))

    for i in robots:
        pos = i[1]
        bathroom[pos[1], pos[0]] = bathroom[pos[1], pos[0]] + 1
    if z >= 7490:
        print(z)
        plt.matshow(bathroom)
        plt.savefig("" + str(z) + ".png")
        plt.clf() 
        plt.cla() 
        plt.close()
        gc.collect()

# Start counting at 0
#7502