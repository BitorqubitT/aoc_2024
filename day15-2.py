import numpy as np
import sys
from pprint import pprint

loc = "data/d15.txt"
np.set_printoptions(threshold=np.inf)
warehouse = []
moves = []

with open(loc) as f:
    for line in f:
        if "#" in line:
            temp_line = ""
            line = line.replace("\n","")
            for symbol in line:
                if symbol == "#":
                    temp_line += "##"
                if symbol == "O":
                    temp_line += "[]"
                if symbol == ".":
                    temp_line += ".."
                if symbol == "@":
                    temp_line += "@."
            warehouse.append(temp_line)
        if "/n" in line:
            continue
        if "#" not in line and line != "\n":
            line = line.replace("\n", "")
            for x in line:
                moves.append(x)

warehouse = np.array([list(row) for row in warehouse])

def get_in_path(matrix, player_position, direction):
    row, col = player_position
    cases = {
        '>': [matrix[row, col:], [(row, c) for c in range(col, matrix.shape[1])]],
        '<': [matrix[row, :col+1], [(row, c) for c in range(col+1)]],
        '^': [matrix[:row + 1, col], [(r, col) for r in range(row + 1)]],
        'v': [matrix[row:, col], [(r, col) for r in range(row, matrix.shape[0])]]
    }
    return cases.get(direction, None)

def check_blocks(start_block, move):
    if move == "v":
        up_or_down = 1
    else:
        up_or_down = -1
    # 32
    new_block = []
    if move == "v":
        for row, col in start_block:
            if warehouse[row + 1, col] in ["]", "#"]:
                #above
                if warehouse[row + 1, col] in ['[', ']', "#"]:
                    new_block.append((row + 1, col))
                if warehouse[row + 1, col - 1] in ['[', ']']:
                    new_block.append((row + 1, col - 1))
            if warehouse[row + 1, col] in ["[", "#"]:
                #above
                if warehouse[row + 1, col] in ['[', ']', "#"]:
                    new_block.append((row + 1, col))
                if warehouse[row + 1, col + 1] in ['[', ']']:
                    new_block.append((row + 1, col + 1))

    if move == "^":
        for row, col in start_block:
            if warehouse[row - 1, col] in ["]", "#"]:
                #above
                if warehouse[row - 1, col] in ['[', ']', "#"]:
                    new_block.append((row - 1, col))
                if warehouse[row - 1, col - 1] in ['[', ']']:
                    new_block.append((row - 1, col - 1))

            if warehouse[row - 1, col] in ["[", "#"]:
                #above
                if warehouse[row - 1, col] in ['[', ']', "#"]:
                    new_block.append((row - 1, col))
                if warehouse[row - 1, col + 1] in ['[', ']']:
                    new_block.append((row - 1, col + 1))
    
    new_block = set(new_block)
    new_block = list(new_block)
    values_above = []
    for location in new_block:
        row, col = location
        values_above.append(warehouse[row][col])

    if "#" in values_above:
        return False
    if "[" not in values_above and "]" not in values_above:
        new_block = []
        new_block.append((start_block[0][0] + up_or_down, start_block[0][1]-1))
        for i in start_block:
            new_block.append((i[0] + up_or_down, i[1]))
        new_block.append((start_block[-1][0] + up_or_down, start_block[-1][1]+1))
        #lets move
        for location in start_block:
            row, col = location
            warehouse[row + up_or_down][col] = warehouse[row, col]
            warehouse[row, col] = "."
        return True
    if "[" in values_above or "]" in values_above:
        x = check_blocks(new_block, move)

    if x:
        new_block = []
        new_block.append((start_block[0][0] + up_or_down, start_block[0][1]-1))
        for i in start_block:
            new_block.append((i[0] + up_or_down, i[1]))
        new_block.append((start_block[-1][0] + up_or_down, start_block[-1][1]+1))
        #lets move
        for location in start_block:
            row, col = location
            warehouse[row + up_or_down][col] = warehouse[row, col]
            warehouse[row, col] = "."
    return x


def check_blocks(start_block, move):
    up_or_down = 1 if move == "v" else -1
    new_block = []

    for row, col in start_block:
        if move == "v":
            if warehouse[row + 1, col] in ["]", "#"]:
                if warehouse[row + 1, col] in ['[', ']', "#"]:
                    new_block.append((row + 1, col))
                if warehouse[row + 1, col - 1] in ['[', ']']:
                    new_block.append((row + 1, col - 1))
            if warehouse[row + 1, col] in ["[", "#"]:
                if warehouse[row + 1, col] in ['[', ']', "#"]:
                    new_block.append((row + 1, col))
                if warehouse[row + 1, col + 1] in ['[', ']']:
                    new_block.append((row + 1, col + 1))
        elif move == "^":
            if warehouse[row - 1, col] in ["]", "#"]:
                if warehouse[row - 1, col] in ['[', ']', "#"]:
                    new_block.append((row - 1, col))
                if warehouse[row - 1, col - 1] in ['[', ']']:
                    new_block.append((row - 1, col - 1))
            if warehouse[row - 1, col] in ["[", "#"]:
                if warehouse[row - 1, col] in ['[', ']', "#"]:
                    new_block.append((row - 1, col))
                if warehouse[row - 1, col + 1] in ['[', ']']:
                    new_block.append((row - 1, col + 1))

    new_block = list(set(new_block))
    values_above = [warehouse[row, col] for row, col in new_block]

    if "#" in values_above:
        return False

    if "[" not in values_above and "]" not in values_above:
        new_block = [(start_block[0][0] + up_or_down, start_block[0][1] - 1)] + \
                    [(i[0] + up_or_down, i[1]) for i in start_block] + \
                    [(start_block[-1][0] + up_or_down, start_block[-1][1] + 1)]
        for row, col in start_block:
            warehouse[row + up_or_down, col] = warehouse[row, col]
            warehouse[row, col] = "."
        return True

    if "[" in values_above or "]" in values_above:
        x = check_blocks(new_block, move)
        if x:
            new_block = [(start_block[0][0] + up_or_down, start_block[0][1] - 1)] + \
                        [(i[0] + up_or_down, i[1]) for i in start_block] + \
                        [(start_block[-1][0] + up_or_down, start_block[-1][1] + 1)]
            for row, col in start_block:
                warehouse[row + up_or_down, col] = warehouse[row, col]
                warehouse[row, col] = "."
    return x



for i in moves:
    player_pos = np.where(warehouse == "@")
    player_pos = (player_pos[0][0], player_pos[1][0])

    move = i
    moves = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
    future_pos = (player_pos[0] + moves[move][0], player_pos[1] + moves[move][1])

    if warehouse[future_pos] == ".":
        #move
        warehouse[future_pos] = "@"
        warehouse[player_pos] = "."

    # we find a wall
    if warehouse[future_pos] == "[" or warehouse[future_pos] == "]":
        in_path_totall = get_in_path(warehouse, future_pos, move)
        in_path_total = in_path_totall[0]
        in_path_position = in_path_totall[1]
            # find all blocks
        
        if move == "v" or move == "^":
           
            give_pos = []
            if warehouse[player_pos[0]+1, player_pos[1]] == "]" and move == "v":
                give_pos.append((player_pos[0]+1, player_pos[1]))
                give_pos.append((player_pos[0]+1, player_pos[1] - 1))
            if warehouse[player_pos[0]+1, player_pos[1]] == "[" and move == "v":
                give_pos.append((player_pos[0]+1, player_pos[1]))
                give_pos.append((player_pos[0]+1, player_pos[1] + 1))
            if warehouse[player_pos[0]-1, player_pos[1]] == "[" and move == "^":
                give_pos.append((player_pos[0]-1, player_pos[1]))
                give_pos.append((player_pos[0]-1, player_pos[1] + 1))
            if warehouse[player_pos[0]-1, player_pos[1]] == "]" and move == "^":
                give_pos.append((player_pos[0]-1, player_pos[1]))
                give_pos.append((player_pos[0]-1, player_pos[1] - 1))

            xx = check_blocks(give_pos, move)
            
            if xx:
                warehouse[future_pos] = "@"
                warehouse[player_pos] = "."
        else:
            if move == "<" or move == "^":
                in_path_total = in_path_total[::-1]
                in_path_position.reverse()

            in_path_pos = []
            in_path = []
            for area in in_path_total:
                if area == "[" or area == "]":
                    in_path.append(area)
                    #easy way to append the position?
                if area == ".":
                    in_path.append(area)
                    break
                if area == "#":
                    in_path.append(area)
                    break
            if in_path[-1] == "#":
                continue
            if in_path[-1] == ".":
                # move every block in_path one position
                change_pos = in_path_position[:len(in_path)]
                for i, old_pos in enumerate(change_pos):
                    if i == 0:
                        warehouse[old_pos[0], old_pos[1]] = "@"
                    else:
                        warehouse[old_pos[0], old_pos[1]] = in_path[i-1]

                warehouse[player_pos[0], player_pos[1]] = "."

box_pos = np.where(warehouse == "[")
total = 0

for y, x in zip(box_pos[0], box_pos[1]):
    score = (y*100) + x 
    total += score

print(total)