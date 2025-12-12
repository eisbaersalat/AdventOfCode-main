import time

s = time.time()
directions = []
with open("2015/03/input.txt", encoding="utf-8") as file:
    directions = file.read()


## PART 1
x = [0,0]
numVisits = dict()

for d in directions:
    if d == "<":
        x[0] -= 1
    elif d == ">":
        x[0] += 1
    elif d == "^":
        x[1] += 1
    elif d == "v":
        x[1] -= 1

    if str(x) in numVisits:
        numVisits[str(x)] += 1
    else:
        numVisits[str(x)] = 1

    

e = time.time()

print(f" {len(numVisits)} houses received a present")
print(f"runtime: {e-s} s")      


 ## PART 2

s = time.time() 

x = [0,0]
y = [0,0]
numVisits = dict()

def visitHouse(s, d):
    global numVisits

    if d == "<":
        s[0] -= 1
    elif d == ">":
        s[0] += 1
    elif d == "^":
        s[1] += 1
    elif d == "v":
        s[1] -= 1

    if str(s) in numVisits:
        numVisits[str(s)] += 1
    else:
        numVisits[str(s)] = 1

    return s

for i in range(0, len(directions)-1, 2):
    x = visitHouse(x, directions[i])
    y = visitHouse(y, directions[i+1])

e = time.time()
print(f" {len(numVisits)} houses received a present with the help of robot-santa")
print(f"runtime: {e-s} s")      