def priority(char):
    if ord(char) < 90:
        return ord(char) - 38
    else:
        return ord(char) - 96


with open("input_small.txt", "r") as file:
    priority_sum = 0
    for line in file:
        stripped_line = line[:-1]
        half_len = len(stripped_line) // 2
        first_pocket = set(stripped_line[:half_len])
        second_pocket = set(stripped_line[half_len:])
        common_item = first_pocket & second_pocket
        priority_sum += priority(common_item.pop())
    print(priority_sum)
