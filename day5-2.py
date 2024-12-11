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

incorrectly_ordered = []
correctly_ordered = []

for some_page_numbers in all_page_numbers:
    legit = True
    for i in range(0, len(some_page_numbers)):
        before = check_before(i, some_page_numbers, rule_set_first)
        after = check_after(i, some_page_numbers, rule_set_last)

        if before is False or after is False:
           legit = False
           
    if legit is False:
        incorrectly_ordered.append(some_page_numbers)

total = 0
for incorrect_page in incorrectly_ordered:

    new_list = []
    for i, number in enumerate(incorrect_page):
        first = number
        new_list.append(first)

        correct = False
        for j in range(0, len(new_list)):
        #while correct is False:
            if first in rule_set_first:
                z = rule_set_first[first]
                index_first = new_list.index(first)
                check = [x for x in new_list[:index_first] if x in z]
                #if new_list[index_first-1] in z:
                if len(check) != 0:
                    new_list.pop(index_first)
                    new_list.insert(index_first-1, first)
                else:
                    correct = True
    correctly_ordered.append(new_list)

    index =  math.ceil(len(new_list) / 2)
    total += new_list[index-1]

print(total) 