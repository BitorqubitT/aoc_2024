import math

loc = "data/d5.txt"

rule_set_first = {}
rule_set_last = {}
page_numbers = False
all_page_numbers = []

# Als we voorkant bekijken dan willen we weten of er iets aan de voorkant had moeten staan.
def check_before(i, some_page_numbers, rule_set_first):
    after = some_page_numbers[i+1:]
    if some_page_numbers[i] in rule_set_first:
        z =  rule_set_first[some_page_numbers[i]]
        check = [x for x in after if x not in z]
        if len(check) != 0:
            return False
    return True

def check_after(i, some_page_numbers, rule_set_last):
    before = some_page_numbers[:i]
    if some_page_numbers[i] in rule_set_last:
        z =  rule_set_last[some_page_numbers[i]]
        check = [x for x in before if x not in z]
        if len(check) != 0:
            return False
    return True

with open(loc) as f:
    for line in f:
        if len(line) == 1:
            page_numbers = True

        if page_numbers is False:
            a = line.replace("\n", "").split("|")
            if int(a[0]) in rule_set_first:
                zz = int(a[1])
                rule_set_first[int(a[0])] = rule_set_first[int(a[0])] + [zz]
            else:
                rule_set_first[int(a[0])] = [int(a[1])]

            if int(a[1]) in rule_set_last:
                zz = int(a[0])
                rule_set_last[int(a[1])] = rule_set_last[int(a[1])] + [zz]
            else:
                rule_set_last[int(a[1])] = [int(a[0])]

        if page_numbers is True and len(line) >= 3:
            line = line.split(",")
            line = [int(x) for x in line]
            all_page_numbers.append(line)

corr = 0
total = 0
for some_page_numbers in all_page_numbers:
    legit = True
    for i in range(0, len(some_page_numbers)):
        before = check_before(i, some_page_numbers, rule_set_first)
        after = check_after(i, some_page_numbers, rule_set_last)

        if before is False or after is False:
           legit = False
           
    if legit:
        corr += 1
        index =  math.ceil(len(some_page_numbers) / 2)
        total += some_page_numbers[index-1]
    
print(total)