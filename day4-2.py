loc = "data/d4.txt"

puzzel = []

with open(loc) as f:
    for line in f:
        line = list(line.replace('\n',""))
        puzzel.append(line)

counter = 0

for y in range(0, len(puzzel[0])):
    for x in range (0, len(puzzel)):
        
        if puzzel[y][x] == "A" and y-1 >= 0 and x-1 >= 0 and y+1 <= len(puzzel[0])-1 and x+1 <=len(puzzel)-1:
            one_max = puzzel[y-1][x-1] + puzzel[y][x] + puzzel[y+1][x+1]
            two_max = puzzel[y-1][x+1] + puzzel[y][x] + puzzel[y+1][x-1]
            if (one_max == "MAS" or one_max == "SAM") and (two_max == "MAS" or two_max == "SAM"):
                counter += 1

print(counter)