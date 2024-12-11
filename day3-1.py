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

total = 0
with open(loc) as f:
    for line in f:
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