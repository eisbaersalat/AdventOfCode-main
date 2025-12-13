import time
import matplotlib.pyplot as plt

start = time.time()
allCommands = []
with open("2015/06/input.txt", encoding="utf-8") as file:
    for line in file:
        tmp = line.rstrip().split(" ")
        if tmp[0] == "toggle":
            allCommands.append(["toggle", tmp[1].split(","), tmp[3].split(",")])
        elif tmp[1] == "on":
            allCommands.append(["on", tmp[2].split(","), tmp[4].split(",")])
        elif tmp[1] == "off":
            allCommands.append(["off", tmp[2].split(","), tmp[4].split(",")])



## PART 1
state = [[False for x in range(0, 1000)] for y in range(1000)]

for c in allCommands:
    x1 = int(c[1][0])
    y1 = int(c[1][1])
    x2 = int(c[2][0])
    y2 = int(c[2][1])

    for xx in range(x1,x2+1):
        for yy in range(y1, y2+1):
            if c[0] == "toggle":
                state[xx][yy] = not state[xx][yy]
            elif c[0] == "on":
                state[xx][yy] = True
            else:
                state[xx][yy] = False
            
result = 0            
for r in state:
    result += sum(r)

plt.figure()
plt.imshow(state)
plt.show()

e = time.time()
print(f" there are {result} lit lights")
print(f"runtime: {e-start} s")      


 ## PART 2

state = [[False for x in range(0, 1000)] for y in range(1000)]

for c in allCommands:
    x1 = int(c[1][0])
    y1 = int(c[1][1])
    x2 = int(c[2][0])
    y2 = int(c[2][1])

    for xx in range(x1,x2+1):
        for yy in range(y1, y2+1):
            if c[0] == "toggle":
                state[xx][yy] += 2
            elif c[0] == "on":
                state[xx][yy] += 1
            else:
                state[xx][yy] -= 1
                state[xx][yy] = max(state[xx][yy], 0)
            
result = 0            
for r in state:
    result += sum(r)

plt.figure()
plt.imshow(state)
plt.show()

e = time.time()
print(f" teh total brightness is {result} ")
print(f"runtime: {e-start} s")      