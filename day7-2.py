from itertools import product

loc = "data/d7.txt"

all_sums = []
operators = ["+", "*", "||"]

total = 0

with open(loc) as f:
    for line in f:
        line = line.replace("\n","").replace(":","").split(" ")
        line = [int(x) for x in line]
        answer = line[0]
        line.pop(0)
        combinations = list(product(operators, repeat=(len(line)-1)))
        expressions = []

        for combination in combinations:
            expression = line[0]
            for i in range(1, len(line)):
                if combination[i-1] == "+":
                    expression += line[i]
                if combination[i-1] == "*":
                    expression *= line[i]
                if combination[i-1] == "||":
                    expression = int(str(expression) + str(line[i]))
            expressions.append(expression)
        
        for expr in expressions:
            if expr == answer:
                total += expr
                break


print(total)

