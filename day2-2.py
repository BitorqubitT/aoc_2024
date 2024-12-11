loc = "data/d2.txt"

safe = 0

with open(loc) as f:
    for line in f:
        line_og = [int(x) for x in line.split()]
        all_versions = []

        for i in range(0, len(line_og)):
            line_not_og = line_og.copy()
            line_not_og.pop(i)
            all_versions.append(line_not_og)

        for line_og in all_versions:
            line_asc = line_og.copy()
            line_des = line_og.copy()
            line_asc.sort()
            line_des.sort(reverse=True)
            if line_og == line_asc or line_og == line_des:
                difference_list = [(abs(line_og[x] - line_og[x + 1])) for x in range(0, len(line_og )-1)]
                difference_list.sort()
                if 0 in difference_list or difference_list[-1] > 3:
                    continue
                else:
                    safe += 1
                    break


print(safe)