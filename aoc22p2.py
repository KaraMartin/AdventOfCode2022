from collections import defaultdict

### Get input.
with open("aoc_22_input.txt", "r") as f:
    s = f.read().rstrip()

### Normalize input.
monkey_map = [row for row in s.split("\n\n")[0].split("\n")]
max_width = max(len(row) for row in monkey_map)

for i,row in enumerate(monkey_map):
    if len(row) < max_width:
        monkey_map[i] += " " * (max_width - len(row))

monkey_path = s.split("\n\n")[1]
curr = []
monkey_instr = []

### Derive instructions from second half of input.
for c in monkey_path:
    if c.isnumeric():
        curr.append(c)
    else:
        monkey_instr.append(int(''.join(curr)))
        monkey_instr.append(c)
        curr = []

if curr:
    monkey_instr.append(int(''.join(curr)))

### Set up current coordinates and track visited coordinates.
init_x, init_y, init_face = 0, monkey_map[0].index('.'), 0
curr_x, curr_y, curr_face = init_x, init_y, init_face
visited = defaultdict()
visited[(init_x, init_y)] = init_face
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

### Helper function for displaying map & visited path.
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

### Helper function for determining cube edge cases.
def check_cube_wrap(tx, ty, face):    
    if ty == -1:
        # E -> A        100->49 , 149->0
        if 100 <= tx < 150:         return 149 - tx, 50, 0
        # F -> A        150->50 , 199->99
        elif 150 <= tx < 200:       return 0, tx - 100, 1

    if ty == 49:
        # A -> E        0->149 , 49->100
        if tx < 50:                 return 149 - tx, 0, 0
        # C -> E        50->0 , 99->49
        elif tx < 100:              return 100, tx - 50, 1
        
    if 0 <= ty <= 49:
        # E -> C        0->50 , 49->99
        if tx == 99:                return 50 + ty, 50, 0
        # F -> B        0->100 , 49->149
        elif tx == 200:             return 0, ty + 100, 1    
        
    if ty == 50:
        # F -> D        150->50 , 199-> 99
        if 150 <= tx <= 200:        return 149, tx - 100, 3

    if ty == 100:
         # C -> B        50->100 , 99->149
        if 50 <= tx < 100:          return 49, tx + 50, 3
        # D -> B        100->49 , 149-> 0
        elif 100 <= tx:             return 149 - tx, 149, 2
        
    if 50 <= ty < 100:
        # A -> F        50->150 , 99->199
        if tx == -1:                return ty + 100, 0, 0
        # D -> F        50->150 , 99->199
        elif tx == 150:             return ty + 100, 49, 2
        
    if 100 <= ty < 150:
        # B -> F        100->0 , 149->49
        if tx == -1:                return 199, ty - 100, 3

        # B -> C        100->50 , 149->99
        elif tx == 50:              return ty - 50, 99, 2

    if ty == 150:
        # B -> D        0 -> 149, 49->100
        if tx <= 50:                return 149 - tx, 99, 2 
        
    return tx, ty, face


### Go instruction by instruction, turning or moving n units. 
for i, inst in enumerate(monkey_instr):
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
            px, py, pf = curr_x, curr_y, curr_face
            
            tx, ty, curr_face = check_cube_wrap((curr_x + dirs[curr_face][0]), (curr_y + dirs[curr_face][1]), curr_face)
            if tx <= -1 or tx >= 200:
                print("x: ", px, py, pf, "\t", dirs[pf], "\t", tx, ty, curr_face)
            if ty <= -1 or ty >= 150:
                print("y: ", px, py, pf, "\t", dirs[pf], "\t",  tx, ty, curr_face)
                
            #print(tx, ty)
            if monkey_map[tx][ty] == '#':
                curr_x, curr_y, curr_face = px, py, pf
                break
            else:
                curr_x, curr_y = tx, ty
                visited[(curr_x, curr_y)] = curr_face

### Output answer.       
#print(f"X: {curr_x}\tY: {curr_y}\t Facing: {curr_face}")
pw = (1000 * (curr_x+1)) + (4 * (curr_y + 1)) + curr_face
print(f"Part 2: Final password on cube map: {pw}")
