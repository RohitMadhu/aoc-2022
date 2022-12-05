elf = []
cal = 0
with open("input.txt", 'r') as f:
    for line in f:
        if len(line.strip()) != 0 :
            cal+=int(line)
        else:
            elf.append(cal)
            cal = 0
sortedelf = sorted(elf)
print(sortedelf)
print((sortedelf[-1]+sortedelf[-2]+sortedelf[-3]))