loc = "data/d19.txt"

patterns2 = []
designs = []

with open(loc) as f:
    found_designs = False
    for line in f:
        if found_designs is False and line != "\n":
            some_patterns = line.split(",")
            patterns2 = patterns2 + [pattern.replace("\n", "").replace(" ", "") for pattern in some_patterns]
        if line == "\n":
            found_designs = True
        elif found_designs:
            designs.append(line.replace("\n",""))
            
def can_construct(target, words):
    if target in words:
        return True
    for word in words:
        if target.startswith(word):
            if can_construct(target[len(word):], words):
                return True
    return False

def filter_smallest_strings(strings):
    strings.sort(key=len)
    smallest_strings = []
    for string in strings:
        if not can_construct(string, smallest_strings):
            smallest_strings.append(string)
    return smallest_strings

patterns = filter_smallest_strings(patterns2)

def match_pattern(design):
    x = False
    if len(design) == 0:
        return True
    pattern_lengths = [1, 2, 3, 4, 5, 6, 7]
    for length in pattern_lengths:
        temp_design = design[:length]
        if temp_design in patterns:
            x = match_pattern(design[length:])
            if x:
                return True
    
possible = 0
for design in designs:
    x = match_pattern(design)
    if x:
        possible += 1
print(possible)



