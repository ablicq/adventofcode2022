def priority(char):
    if ord(char) <= 90:
        return ord(char) - 38
    else:
        return ord(char) - 96


with open("day3/input.txt", "r") as file:
    priority_sum = 0
    cpt = 0
    while True:
        l1 = file.readline()[:-1]
        if len(l1) == 0:
            break
        l2 = file.readline()[:-1]
        l3 = file.readline()[:-1]

        first_elf = set(l1)
        second_elf = set(l2)
        third_elf = set(l3)

        common_item = first_elf & second_elf & third_elf
        priority_sum += priority(common_item.pop())
    print(priority_sum)
