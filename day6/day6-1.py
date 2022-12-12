with open("day6/input.txt", "r") as file:
    line = file.readline()
    for pos, char in enumerate(line):
        start = max(0, pos - 4)
        if len(set(line[start:pos])) == 4:
            print(pos)
            break
