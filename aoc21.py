from collections import defaultdict

s = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

with open("aoc_21_input.txt", "r") as f:
    s = f.read().strip()

def evaluate(left, operation, right):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == "*":
        return left * right
    elif operation == "/":
        return int(left / right)
    print("ERROR!")

data = [[y for y in x.split(": ")] for x in s.strip().split("\n")]

nums = defaultdict()
both_unknown = []
one_unknown = []
ops_stack = []

for i,d in enumerate(data):
    if d[1].isnumeric():
        nums[data[i][0]] = int(data[i][1])
    else:
        l, op, r = data[i][1].split(" ")
        if l in nums:
            if r in nums:
                nums[data[i][0]] = evaluate(nums[l], op, nums[r])
            else:
                one_unknown.append([data[i][0], l, op, r])
        else:
            if r in nums:
                one_unknown.append([data[i][0], l, op, r])
            else:
                both_unknown.append([data[i][0], l, op, r])

#print("Processed")
#print("both unknown: ", len(both_unknown))
#print("one unknown: ", len(one_unknown))


while both_unknown:
    if one_unknown:
        temp = []
        while one_unknown:
            monkey, l, op, r = one_unknown.pop()
            if l in nums and r in nums:
                nums[monkey] = evaluate(nums[l], op, nums[r])
            else:
                temp.append([monkey, l, op, r])
        one_unknown = temp

    if both_unknown:
        temp = []
        while both_unknown:
            monkey, l, op, r = both_unknown.pop()
            if l in nums and r in nums:
                nums[monkey] = evaluate(nums[l], op, nums[r])
            elif l in nums or r in nums:
                one_unknown.append([monkey, l, op, r])
            else:
                temp.append([monkey, l, op, r])
        both_unknown = temp

while one_unknown:
    temp = []
    while one_unknown:
        monkey, l, op, r = one_unknown.pop()
        if l in nums and r in nums:
            nums[monkey] = evaluate(nums[l], op, nums[r])
        else:
            temp.append([monkey, l, op, r])
    one_unknown = temp

print(f"Part 1: {nums['root']}")
