import time
import re

## PART 1
with open("day6/input.txt", encoding="utf-8") as file:
    calcInput = [line.rstrip().lstrip() for line in file]

s = time.time()

rx = ' +'
n1 = re.split(rx, calcInput[0])
n2 = re.split(rx, calcInput[1])
n3 = re.split(rx, calcInput[2])
n4 = re.split(rx, calcInput[3])
op = re.split(rx, calcInput[4])



r = []
sumAll = 0
for i in range(0, len(n1)):
    _r = eval(n1[i] + op[i] + n2[i] + op[i] + n3[i] + op[i] + n4[i])
    r.append(_r)
    sumAll += _r

e = time.time()

print()
print("P1: Answer is " + str(sumAll))
print()
print("Time taken: " + str(e - s) + " seconds")



## PART 2
with open("day6/input.txt", encoding="utf-8") as file:
    calcInput = [line for line in file]

def doMath(listOfStr, op):

    n = len(listOfStr[0])

    if op == "+":
        r = 0
        for i in range(n):
            s = [l[i] for l in listOfStr]
            num = int("".join(s).lstrip().rstrip())
            r += num

    elif op == "*":
        r = 1
        for i in range(n):
            s = [l[i] for l in listOfStr]
            num = int("".join(s).lstrip().rstrip())
            r *= num

    return r
    
            

s = time.time()

i = 0
lastIdx = -1
sumResult = 0
while i < len(calcInput[0]):

    allSpaces = True
    for l in calcInput:
        if l[i] != " ":
            allSpaces = False
            break
    
    # last loop
    if i == len(calcInput[0])-1:
        allSpaces = True        

    if allSpaces:
        # all spaces -> new computation
      
        op = calcInput[-1][lastIdx+1]
        allStr = [line[lastIdx+1:i] for line in calcInput[0:-1]]
        sumResult += doMath(allStr, op)

        lastIdx = i
    i += 1


e = time.time()

print()
print("P2: Answer is " + str(sumResult))
print()
print("Time taken: " + str(e - s) + " seconds")