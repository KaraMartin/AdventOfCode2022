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
root_left, root_right = "", ""

for i,d in enumerate(data):
    if d[1].isnumeric():
        nums[data[i][0]] = int(data[i][1])
    else:
        l, op,  r = data[i][1].split(" ")
        if data[i][0] == "root":
            root_left = l
            root_right = r
        else:
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

#print(root_left, root_right)

nums["humn"] = 'x'

# binary search on x?
def bin_search_x(nums, one_unknown, both_unknown):
    L = -1000000000000000
    R = 10000000000000000
    
    while L <= R:
        mid = (L + R) // 2
        #print(L, mid, R, end="\t")
        nums["humn"] = mid
        n = {key: value for key, value in nums.items()}
        b = both_unknown.copy()
        o = one_unknown.copy()
        while b:
            if o:
                temp = []
                while o:
                    monkey, l, op, r = o.pop()
                    if l in n and r in n:
                        n[monkey] = evaluate(n[l], op, n[r])
                    else:
                        temp.append([monkey, l, op, r])
                o = temp

            if b:
                temp = []
                while b:
                    monkey, l, op, r = b.pop()
                    if l in n and r in n:
                        n[monkey] = evaluate(n[l], op, n[r])
                    elif l in n or r in n:
                        o.append([monkey, l, op, r])
                    else:
                        temp.append([monkey, l, op, r])
                b = temp

        while o:
            temp = []
            while o:
                monkey, l, op, r = o.pop()
                if l in n and r in n:
                    n[monkey] = evaluate(n[l], op, n[r])
                else:
                    temp.append([monkey, l, op, r])
            o = temp

        if n[root_left] == n[root_right]:
            return mid
        elif n[root_left] > n[root_right]:
            L = mid + 1
        else:
            R = mid - 1

print(f"Part 2: {bin_search_x(nums, one_unknown, both_unknown)}")
