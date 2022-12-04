'''
    * Each rucksack has 2 large compartments
    * All items of a type meant to go in exactly one of the two compartments
    * one mistake per rucksack
    * Each item a-zA-Z case-sensitive
    
    * Each rucksack a line of text; the items characters
    * first half first compartment, second second

'''
from collections import Counter
def main():
    res = 0
    mapping = { **{chr(a + 97): a+1 for a in range(26)}, **{chr(a + 65): a+27 for a in range(26)} }
    #print(mapping)
    with open("aoc_03_input.txt", "r") as fp:
        lines = fp.readlines()
        for i in range(0, len(lines), 3):
            first = Counter(lines[i])
            second = Counter(lines[i+1])
            third = Counter(lines[i+2])
            curr = list(first & second & third)[0]
            res += mapping[curr]          

    print(f"Sum is {res}")

if __name__ == "__main__":
    main()