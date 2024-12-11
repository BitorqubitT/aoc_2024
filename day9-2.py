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

all_filenumbers = list(set(disk))
all_filenumbers.remove("")
all_filenumbers.remove(0)
all_filenumbers.reverse()

for filename in all_filenumbers:
    space_needed = len([i for i, x in enumerate(disk) if x == filename])
    pos_to_remove = [i for i, x in enumerate(disk) if x == filename]
    #lets find the space on disk
    space_counter = 0
    start_space_counting = False
    free_positions = []
    found_space = False
    for pos, file_name in enumerate(disk):
        if space_counter == space_needed:
            found_space = True
            break
        elif file_name == "" and start_space_counting is False:
            start_space_counting = True
            space_counter += 1
            free_positions.append(pos)
        elif file_name == "" and start_space_counting:
            space_counter += 1
            free_positions.append(pos)
        elif file_name != "" and start_space_counting:
            start_space_counting = False
            space_counter = 0
            free_positions = []
        elif pos in pos_to_remove:
            break
 
    if found_space:
        for pos in free_positions:
            disk[pos] = filename
        for pos in pos_to_remove:
            disk[pos] = ""

checksum = 0
for i, number in enumerate(disk):
    if number != "":
        checksum += i*number

print(checksum)
            







