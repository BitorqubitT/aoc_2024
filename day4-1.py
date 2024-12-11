loc = "data/d4.txt"

puzzel = []

with open(loc) as f:
    for line in f:
        line = list(line.replace('\n',""))
        puzzel.append(line)

counter = 0
all_possibilites = []
for y in range(0, len(puzzel[0])):
    for x in range (0, len(puzzel)):
        if x + 4 <= len(puzzel[0]):
            word = "".join(puzzel[y][x:x+4])
            all_possibilites.append(word)
        
        if x - 3 >= 0:
            word = "".join(puzzel[y][x-3:x+1])
            word = word[::-1]
            all_possibilites.append(word)

        if y + 4 <= len(puzzel):
            word = puzzel[y][x] + puzzel[y+1][x] + puzzel[y+2][x] + puzzel[y+3][x]
            all_possibilites.append(word)

        if y - 3 >= 0:
            word = puzzel[y][x] + puzzel[y-1][x] + puzzel[y-2][x] + puzzel[y-3][x]
            all_possibilites.append(word)

        if x + 4 <= len(puzzel[0]) and y + 4 <= len(puzzel):
            word = puzzel[y][x] + puzzel[y+1][x+1] + puzzel[y+2][x+2] + puzzel[y+3][x+3]
            all_possibilites.append(word)

        if x - 3 >= 0 and y - 3 >= 0:
            word = puzzel[y][x] + puzzel[y-1][x-1] + puzzel[y-2][x-2] + puzzel[y-3][x-3]
            all_possibilites.append(word)

        if x + 4 <= len(puzzel[0]) and y - 3 >= 0:
            word = puzzel[y][x] + puzzel[y-1][x+1] + puzzel[y-2][x+2] + puzzel[y-3][x+3]
            all_possibilites.append(word)

        if y + 4 <= len(puzzel) and x - 3 >= 0:
            word = puzzel[y][x] + puzzel[y+1][x-1] + puzzel[y+2][x-2] + puzzel[y+3][x-3]
            all_possibilites.append(word)

for i in all_possibilites:
    if i == "XMAS":
        counter += 1

print(counter)