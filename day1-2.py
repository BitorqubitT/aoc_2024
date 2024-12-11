loc = "data/d1.txt"

list_one = []
list_two = []

with open(loc) as f:
    for line in f:
        list_one.append(int(line.split()[0]))
        list_two.append(int(line.split()[1]))

total_distance = 0

for number in list_one:
    number_of_occurences = list_two.count(number)
    total_distance += number_of_occurences * number

print(total_distance)