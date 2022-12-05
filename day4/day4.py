
counter1 = 0
counter2 = 0    
with open("input.txt", 'r') as f:
    for line in f:
        pair = line.split(",")
        first = pair[0].split("-")
        second = pair[1].split("-")
        firstAssign = list(range(int(first[0]), int(first[1])+1))
        secondAssign = list(range(int(second[0]), int(second[1])+1))
        if all(item in firstAssign for item in secondAssign) or all(item in secondAssign for item in firstAssign):
            counter1+=1
        if any((match := item) in firstAssign for item in secondAssign) or any((match := item) in secondAssign for item in firstAssign):
            counter2+=1
print("#1:", counter1)
print("#2:", counter2)
