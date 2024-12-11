loc = "data/d3.txt"

def find_mul(line):
    all_parts = [] 
    for i in range(0, len(line) - 4):
        if line[i:i+4] == 'mul(':
            for j in range(0, len(line) - i):
                if line[i+j] == ")":
                    found = i+j+1
                    all_parts.append(line[i:found])
                    break
    return all_parts

def find_do(line):
    all_do = []
    mul = True
    temp = ""
    for i in range(0, len(line)):
        if mul:
            temp += line[i]
        if mul and line[i:i+7] == "don't()":
            all_do.append(temp)
            temp = ""
            mul = False
        if line[i:i+4] == "do()":
            mul = True
        if i == len(line) - 1:
            all_do.append(temp)
    return all_do

total = 0
linee = ""
with open(loc) as f:
    for line in f:
        linee += line
    all_do = find_do(linee)
    #print(all_do)
    for line in all_do:
        all_muls= find_mul(line)
        for mul in all_muls:
            mul = mul.replace("mul(", "")
            mul = mul.replace(")", "")
            split_mul = mul.split(",")
            if len(split_mul) == 2:
                try:
                    total += int(split_mul[0]) * int(split_mul[1])
                except:
                    continue
print(total)