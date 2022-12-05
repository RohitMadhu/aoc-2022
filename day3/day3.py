# Part 1
chrList = []
prior = list(range(1, 27))
score = 0

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))
        
for c in range_char("a", "z"):
    chrList.append(c)

priorDict = dict(zip(chrList, prior))

with open("input.txt", 'r') as f:
    for line in f:
        c1 = list(line.strip())[0:int((len(line)-1)/2)]
        c2 = list(line.strip())[int((len(line)-1)/2):(len(line)-1)]
        result = (set(c1) & set(c2)).pop()
        if(result.isupper() != True):
            score += priorDict[result]
        else:
            score += priorDict[result.lower()] + 26
print("Final Score 1:",score)

# Part 2
score2 = 0
with open("input.txt", 'r') as f:
    for line in f:
        res = (set(list(line.strip())) & set(list(next(f).strip())) & set(list(next(f).strip()))).pop()
        if(res.isupper() != True):
            score2 += priorDict[res]
        else:
            score2 += priorDict[res.lower()] + 26
print("Final Score 2:",score2)
