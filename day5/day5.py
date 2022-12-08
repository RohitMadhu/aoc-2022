import re
ship = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

with open("input.txt", 'r') as f:
    for line in f:
        if(line !="\n" and "move" not in line):
            layer = list(line.replace("["," ").replace("]"," ").strip())
            sec = 1
            res = []
            for idx, e in enumerate(layer):
                if(e != ' ' and sec <= 9 and e.isdigit() == False):
                    ship[sec].append(layer[idx])
                    sec+=1
                elif(idx%4 == 0):
                    sec+=1
        elif("move" in line):
            moves = re.findall('\d+', line)
            #move to = creating slice of dictionary list and adding to original move to list
            pkg = ship[int(moves[1])][0:int(moves[0])]
            #print("pkg: ", pkg[::-1])
            ship[int(moves[2])] = ship[int(moves[1])][0:int(moves[0])] + ship[int(moves[2])]
            #remove to = creating slice of dictionary list 
            ship[int(moves[1])] = ship[int(moves[1])][int(moves[0]):]

print(ship)

#for part1
# reverse the pkg[::-1]
