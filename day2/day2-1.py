score_dict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

with open("input.txt", "r") as file:
    my_score = 0
    for line in file:
        my_score += score_dict[line[:3]]
    print(my_score)
