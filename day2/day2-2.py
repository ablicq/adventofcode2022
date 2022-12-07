score_dict = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

with open("input.txt", "r") as file:
    my_score = 0
    for line in file:
        my_score += score_dict[line[:3]]
    print(my_score)
