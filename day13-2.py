import numpy as np
loc = "data/d13.txt"

counter = 0

all_system = []

with open(loc) as f:
    system = []
    system_one = []
    system_two = []
    result = []
    for line in f:
        counter += 1
        if "A" in line or "B" in line:
            line = line.strip().split(" ")[2:]
            system_one.append(float(line[0].replace("X+","").replace(",","")))
            system_two.append(float(line[1].replace("Y+","")))
        if "Prize" in line:
            prices = line.strip().split(" ")
            result.append(float(prices[1].replace("X=","").replace(",","")) + 10000000000000)
            result.append(float(prices[2].replace("Y=","")) + 10000000000000)
        if line == "\n":
            all_system.append([system_one, system_two, result])
            system_one, system_two, result = [], [], []

    all_system.append([system_one, system_two, result])

total_tokens = 0
for system_one, system_two, result in all_system:
    A = np.array([system_one, system_two])
    B = np.array(result)
    solution = np.linalg.solve(A, B)

    if all(round(val, 4).is_integer() for val in solution):
        total_cost = solution[0] * 3 + solution[1] * 1
        total_tokens += total_cost

print(total_tokens)