# Now X -> Lose
#     Y -> Draw
#     Z -> Win 

with open("aoc_02_input.txt", "r") as fp:
    lines = fp.readlines()
    res = 0
    for line in lines:
        choices = line.split()

        # villain Rock
        if choices[0] == "A":
            if choices[1] == "X":       # Hero Lose     ==> Scissors
                res += 3                #   0 + 3
            elif choices[1] == "Y":     # Hero Draw     ==> Rock
                res += 4                #   3 + 1
            else:                       # Hero Win      ==> Paper
                res += 8                #   6 + 2

        # villain Paper
        elif choices[0] == "B":
            if choices[1] == "X":       # Hero Lose     ==> Rock
                res += 1                #   0 + 1
            elif choices[1] == "Y":     # Hero Draw     ==> Paper
                res += 5                #   3 + 2
            else:                       # Hero Win      ==> Scissors
                res += 9                #   6 + 3

        # villain Scissors
        elif choices[0] == "C":
            if choices[1] == "X":       # Hero Lose     ==> Paper
                res += 2                #   0 + 2
            elif choices[1] == "Y":     # Hero Draw     ==> Scissors
                res += 6                #   3 + 3
            else:                       # Hero Win      ==> Rock
                res += 7                #   6 + 1

print(f"Total score: {res}")