import numpy as np
import heapq

loc = "data/d18.txt"

moves = []

with open(loc) as f:
    for line in f:
        move = line.split(",")
        moves.append((int(move[0]), int(move[1])))

ram = np.full((71, 71), ".")

for x, y in moves:
    ram[y, x] = "#"

    # Dijkstra's algorithm to find the shortest path in a maze
    def dijkstra(maze, start, end):
        rows, cols = maze.shape
        distances = np.full((rows, cols), np.inf)
        distances[start] = 0
        direction = (0, 1)
        priority_queue = [(0, start, direction)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        while priority_queue:
            current_distance, (current_row, current_col), direction = heapq.heappop(priority_queue)

            if (current_row, current_col) == end:
                break

            for dr, dc in directions:
                neighbor_row, neighbor_col = current_row + dr, current_col + dc
                new_direction = (dr, dc)
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and maze[neighbor_row, neighbor_col] != "#":
                    distance = current_distance + 1
                    if distance < distances[neighbor_row, neighbor_col]:
                        shortest_direction = (dr, dc) 
                        distances[neighbor_row, neighbor_col] = distance
                        heapq.heappush(priority_queue, (distance, (neighbor_row, neighbor_col), new_direction))
            direction = shortest_direction

        return distances[end]

    # Define start and end points
    start = (0, 0)
    end = (70, 70)

    # Find the shortest path
    shortest_path_distance = dijkstra(ram, start, end)
    if shortest_path_distance == np.inf:
        print(x, y)
        break