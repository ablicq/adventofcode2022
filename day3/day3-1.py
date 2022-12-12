def priority(char):
    if ord(char) <= 90:
        return ord(char) - 38
    else:
        return ord(char) - 96


with open("day3/input.txt", "r") as file:
    priority_sum = 0
    for line in file:
        l = line[:-1]
        half_len = len(l) // 2
        first_pocket = set(l[:half_len])
        second_pocket = set(l[half_len:])
        common_item = first_pocket & second_pocket
        priority_sum += priority(common_item.pop())
    print(priority_sum)
