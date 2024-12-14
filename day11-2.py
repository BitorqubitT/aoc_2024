loc = "data/d11.txt"

stones = {}

with open(loc) as f:
    for line in f:
        line = [x for x in line.split(" ")]
        for stone in line:
            if stone in stones:
                stones[stone] = stones[stone] + 1
            else:
                stones[stone] = 1

print(stones)

def blink(stones):
    new_stones = {}
    for stone in stones:
        if stone == "0":
            if "1" in new_stones:
                new_stones["1"] = stones[stone] + new_stones["1"]
            else:
                new_stones["1"] = stones[stone]
        elif len(stone) % 2 == 0:
            split_stone = [stone[:int(len(stone)/2)], stone[int(len(stone)/2):]]
            for a in split_stone:
                while len(a) > 1 and a[0] == "0":
                    a = a[1:]
                if a in new_stones:
                    new_stones[a] = stones[stone] + new_stones[a]
                else:
                    new_stones[a] = stones[stone]
        else:
            if str(int(stone)*2024) in new_stones:
                new_stones[str(int(stone)*2024)] = stones[str(int(stone)*2024)] + stones[stone]
            else:
                new_stones[str(int(stone)*2024)] = stones[stone]
    return new_stones    

for blinks in range(0, 75):
    stones = blink(stones)

total = 0
total = sum([total+stones[x] for x in stones])
print(total)