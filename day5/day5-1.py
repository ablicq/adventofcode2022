from collections import defaultdict, deque


def move(n, src, dst):
    for _ in range(n):
        dst.append(src.pop())


def process_stacks(line, stacks):
    for pos, char in enumerate(line):
        if 65 <= ord(char) <= 90:
            i = pos // 4
            stacks[i].appendleft(char)


def convert_stacks(stacks):
    return [stacks[i] for i in range(len(stacks))]


def process_moves(line, stacks):
    _, n, _, src, _, dst = line.split()
    move(int(n), stacks[int(src) - 1], stacks[int(dst) - 1])


with open("day5/input.txt", "r") as file:
    file_part = "stacks"
    stacks = defaultdict(deque)
    for line in file:
        if line == "\n":
            file_part = "moves"
            stacks = convert_stacks(stacks)
            continue

        if file_part == "stacks":
            process_stacks(line, stacks)
            continue

        if file_part == "moves":
            process_moves(line, stacks)

    print("".join([s.pop() for s in stacks]))
