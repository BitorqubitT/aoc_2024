loc = "data/d11.txt"

with open(loc) as f:
    for line in f:
        stones = [x for x in line.split(" ")]

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            split_stone = [stone[:int(len(stone)/2)], stone[int(len(stone)/2):]]
            for a in split_stone:
                while len(a) > 1 and a[0] == "0":
                    a = a[1:]
                new_stones.append(a)
        else:
            new_stones.append(str(int(stone)*2024))
    return new_stones    

for blinks in range(0, 25):
    stones = blink(stones)
    print(len(stones))