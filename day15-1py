import numpy as np

loc = "data/d15.txt"

warehouse = []
moves = []
with open(loc) as f:
    for line in f:
        if "#" in line:
            warehouse.append(line.replace("\n",""))
        if "/n" in line:
            continue
        if "#" not in line and line != "\n":
            line = line.replace("\n", "")
            for x in line:
                moves.append(x)

warehouse = np.array([list(row) for row in warehouse])

counter = 0 
for i in moves:
    counter += 1
    player_pos = np.where(warehouse == "@")
    player_pos = (player_pos[0][0], player_pos[1][0])

    move = i
    moves = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
    future_pos = (player_pos[0] + moves[move][0], player_pos[1] + moves[move][1])

    # Define a function to get positions based on direction
    def get_in_path(matrix, player_position, direction):
        row, col = player_position
        cases = {
            '>': [matrix[row, col:], [(row, c) for c in range(col, matrix.shape[1])]],
            '<': [matrix[row, :col+1], [(row, c) for c in range(col+1)]],
            '^': [matrix[:row + 1, col], [(r, col) for r in range(row + 1)]],
            'v': [matrix[row:, col], [(r, col) for r in range(row, matrix.shape[0])]]
        }
        return cases.get(direction, None)

    if warehouse[future_pos] == ".":
        warehouse[future_pos] = "@"
        warehouse[player_pos] = "."

    if warehouse[future_pos] == "O":
        in_path_totall = get_in_path(warehouse, future_pos, move)
        in_path_total = in_path_totall[0]
        in_path_position = in_path_totall[1]
        if move == "<" or move == "^":
            in_path_total = in_path_total[::-1]
            in_path_position.reverse()

        in_path_pos = []
        in_path = []
        for area in in_path_total:
            if area == "O":
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
                    warehouse[old_pos[0], old_pos[1]] = "O"

            warehouse[player_pos[0], player_pos[1]] = "."

box_pos = np.where(warehouse == "O")
total = 0

for y, x in zip(box_pos[0], box_pos[1]):
    score = (y*100) + x 
    total += score

print(total)