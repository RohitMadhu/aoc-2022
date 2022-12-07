#Part 1
count = 0
with open("input.txt", 'r') as f:
    for line in f:
        chars = list(line)
        marker = []
        for i in chars:
            count+=1
            if len(marker) < 4:
                marker.append(i)
            elif len(set(marker)) != 4:
                marker.pop(0)
                marker.append(i)
            if len(set(marker)) == 4:
                print(marker,count)
                break

#Part 2
count = 0
with open("input.txt", 'r') as f:
    for line in f:
        chars = list(line)
        marker = []
        for i in chars:
            count+=1
            if len(marker) < 14:
                marker.append(i)
            elif len(set(marker)) != 14:
                marker.pop(0)
                marker.append(i)
            if len(set(marker)) == 14:
                print(marker,count)
                break
