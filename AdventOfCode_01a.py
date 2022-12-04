# Find the Elf carrying the most Calories --
# How many total Calories is that Elf carrying?

best, curr = 0,0

with open("aoc_01_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            if curr > best: best = curr
            curr = 0
        else:
            curr += int(line)
        
print(f"Best: {best}")
