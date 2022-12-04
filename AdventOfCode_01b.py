from heapq import heappop, heappush

res = []

with open("aoc_01_input.txt", "r") as fp:
    lines = fp.readlines()
    curr = 0
    for line in lines:
        if line == "\n":
            heappush(res, -1 * curr)
            curr = 0
        else:
            curr += int(line)
    
    best_three = heappop(res) + heappop(res) + heappop(res)
    print(f"Best Sum of Three: {-1 * best_three}")