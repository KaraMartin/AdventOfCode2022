from collections import defaultdict

'''
s="""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
'''

with open("aoc_22_input.txt", "r") as f:
    s = f.read().rstrip()

monkey_map = [row for row in s.split("\n\n")[0].split("\n")]
max_width = max(len(row) for row in monkey_map)

for i,row in enumerate(monkey_map):
    if len(row) < max_width:
        monkey_map[i] += " " * (max_width - len(row))

monkey_path = s.split("\n\n")[1]
curr = []
monkey_instr = []

for c in monkey_path:
    if c.isnumeric():
        curr.append(c)
    else:
        monkey_instr.append(int(''.join(curr)))
        monkey_instr.append(c)
        curr = []

if curr:
    monkey_instr.append(int(''.join(curr)))

init_x, init_y, init_face = 0, monkey_map[0].index('.'), 0
curr_x, curr_y, curr_face = init_x, init_y, init_face
visited = defaultdict()
visited[(init_x, init_y)] = init_face
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_mmap(mmap, visited):
    for i,r in enumerate(mmap):
        for j,c in enumerate(r):
            if (i,j) in visited:
                if visited[(i,j)] == 0:
                    print('>', end="")
                elif visited[(i,j)] == 1:
                    print('v', end="")
                elif visited[(i,j)] == 2:
                    print('<', end="")
                elif visited[(i,j)] == 3:
                    print('^', end="")
            else:
                print(c, end="")
        print()
                    
for inst in monkey_instr:
    if inst == 'R':
        curr_face += 1
        curr_face %= 4
        visited[(curr_x, curr_y)] = curr_face
    elif inst == 'L':
        curr_face -= 1
        curr_face %= 4
        visited[(curr_x, curr_y)] = curr_face
    else:
        for n in range(0, inst):
            tx = (curr_x + dirs[curr_face][0]) % (len(monkey_map))
            ty = (curr_y + dirs[curr_face][1]) % (max_width)
            if monkey_map[tx][ty] == '#':
                break
            elif monkey_map[tx][ty] == ' ':                
                # wrap around
                px, py = curr_x, curr_y
                while monkey_map[tx][ty] == ' ':
                    curr_x, curr_y = tx, ty
                    tx = (curr_x + dirs[curr_face][0]) % (len(monkey_map))
                    ty = (curr_y + dirs[curr_face][1]) % (max_width )
                if monkey_map[tx][ty] == '#':
                    curr_x, curr_y = px, py
                    break
                else:
                    curr_x, curr_y = tx, ty
                    visited[(curr_x, curr_y)] = curr_face
            else:
                curr_x, curr_y = tx, ty
                visited[(curr_x, curr_y)] = curr_face

#print_mmap(monkey_map, visited)
#print(f"X: {curr_x}\tY: {curr_y}\t Facing: {curr_face}")
pw = (1000 * (curr_x+1)) + (4 * (curr_y + 1)) + curr_face
print(f"Part 1: Final password on flat map: {pw}")
