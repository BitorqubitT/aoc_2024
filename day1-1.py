loc = "data/d1.txt"

list_one = []
list_two = []

with open(loc) as f:
    for line in f:
        list_one.append(int(line.split()[0]))
        list_two.append(int(line.split()[1]))

list_one.sort()
list_two.sort()

total_distance = 0

for i, number in enumerate(list_one):
    difference = abs(number - list_two[i])
    total_distance += difference

print(total_distance)
