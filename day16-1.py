import heapq
import numpy as np

loc = "data/test.txt"

maze = []
with open(loc) as f:
    for line in f:
        maze.append(line.replace("\n",""))

maze = np.array([list(row) for row in maze])

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
                if direction != new_direction:
                    penal = 1000
                else:
                    penal = 0
                distance = current_distance + 1 + penal
                if distance < distances[neighbor_row, neighbor_col]:
                    shortest_direction = (dr, dc) 
                    distances[neighbor_row, neighbor_col] = distance
                    heapq.heappush(priority_queue, (distance, (neighbor_row, neighbor_col), new_direction))
        direction = shortest_direction

    return distances[end]

# Define start and end points
player_pos = np.where(maze == "S")
start = (player_pos[0][0], player_pos[1][0])

player_pos = np.where(maze == "E")
end = (player_pos[0][0], player_pos[1][0])

# Find the shortest path
shortest_path_distance = dijkstra(maze, start, end)
print("Shortest path distance:", shortest_path_distance)
