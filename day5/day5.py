ship = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}
with open("input.txt", 'r') as f:
    for line in f:
        if(line !="\n"):
            layer = list(line.replace("["," ").replace("]"," ").strip())
            sec = 1
            res = []
            for idx, e in enumerate(layer):
                if(e != ' ' and sec <= 9 and e.isdigit() == False):
                    ship[str(sec)].append(layer[idx])
                    sec+=1
                elif(idx%4 == 0):
                    sec+=1
        else:
            break
print(ship)
