def fully_overlap(a1l, a1h, a2l, a2h):
    if a1l <= a2l:
        return a1h >= a2h
    else:
        return a2h <= a1h


with open("day4/input.txt", "r") as file:
    cpt = 0
    for line in file:
        l = line[:-1]
        a1, a2 = l.split(",")
        a1l, a1h = a1.split("-")
        a2l, a2h = a2.split("-")
        a1l, a1h, a2l, a2h = int(a1l), int(a1h), int(a2l), int(a2h)
        cpt += fully_overlap(a1l, a1h, a2l, a2h)
    print(cpt)
