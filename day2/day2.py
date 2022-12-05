#Part 1:
score = 0
strat = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

with open("input.txt", 'r') as f:
    for line in f:
        contents = line.strip().split(" ")
        op = strat.get(contents[0])
        you = strat.get(contents[1])
        if (op == 3 and you == 1) or (op == 1 and you == 2) or (op == 2 and you == 3):
            score += you + 6
        elif you == op: 
            score += you + 3
        else:
            score += you
print("final score:", score)

#Part 2:
score = 0
strat = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}

with open("input.txt", 'r') as f:
    for line in f:
        contents = line.strip().split(" ")
        op = strat.get(contents[0])
        end = strat.get(contents[1])
        if end == 6:
            if (op == 1):
                score += 2 + end
            elif (op == 2):
                score += 3 + end
            else:
                score += 1 + end
        elif end == 3: 
            score += op + end
        else:
            if (op == 1):
                score += 3 + end
            elif (op == 2):
                score += 1 + end
            else:
                score += 2 + end
print("final score:", score)
