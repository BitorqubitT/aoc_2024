loc = "data/d9.txt"

with open(loc) as f:
    for line in f:
        line.replace("\n", "")
        disk_map = [x for x in line]

disk = []

file_id = 0
for i, number in enumerate(disk_map):
    if i%2 != 0:
        for amount_of_files in range(0, int(number)):
            disk.append("")
    else:
        for amount_of_files in range(0, int(number)):
            disk.append(file_id)
        file_id += 1

full = False

while full is False:
    last_file = disk[-1]
    try:
        first_empty_spot = disk.index("")
    except:
        full = True
        break
    disk[first_empty_spot] = last_file
    disk.pop()

checksum = 0
for i, number in enumerate(disk):
    checksum += i*number

print(checksum)
