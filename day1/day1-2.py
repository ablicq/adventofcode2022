from heapq import nlargest

with open("input.txt", "r") as file:
    elves = []
    current_elf = 0
    for line in file:
        if line == "\n":
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    print(sum(nlargest(3, elves)))