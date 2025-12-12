import time
import math
import itertools
import numpy as np
from z3Optimizer import solveFastestPath


light_target = []
buttons = []
joltage_req = []

with open("day10/input.txt", encoding="utf-8") as file:
    for line in file:
        lights, rest = line.split(']')
        light_target.append(lights[1:])

        butt, jolt = rest.split('{')
        buttons.append(butt[1:-1])
        joltage_req.append(jolt.split('}')[0])
        a = 4

for idx, jolts in enumerate(joltage_req):
    joltage_req[idx] = list( map(int, jolts.split(',') ) )

for idx,light in enumerate(light_target):
    tmp = []
    for l in light:
        if l == ".":
            tmp.append(False)
        elif l == "#":
            tmp.append(True)
    light_target[idx] = tmp

for idx,butt in enumerate(buttons):
    tmp = butt.split(" ")
    tmpB = []
    for b in tmp:
        b = b.replace("(", "").replace(")", "")
        tmpB.append(list( map(int, b.split(",") ) ))

    buttons[idx] = tmpB


def getShortestSolutionForMachine(light_target, buttons ):
    nButtons = len(buttons) 
    for numCom in range(1, nButtons):
        combToTest = list( itertools.combinations(list(range(nButtons)), numCom) )

        for comb in combToTest:

            # start with false
            state = [False]*len(light_target)

            # iterate through all buttons in this combination
            for b in comb:

                # iterate through all lights that this button operates
                for l in buttons[b]:
                    state[l] = not state[l]

            if state == light_target:
                return comb


## ---------------PART 1 -----------------
s = time.time()

pressesPerMachine = []

for machine in range(0, len(light_target)):
    r = getShortestSolutionForMachine(light_target[machine], buttons[machine])
    pressesPerMachine.append(len(r))

overallPresses = sum(pressesPerMachine)
    



e = time.time()
print()
print(f"P1: {overallPresses} button operations are needed")
print("Time taken: " + str(e - s) + " seconds")

## ---------------PART 2 -----------------
s = time.time()

allSum = 0

for idx in range(len(joltage_req)):
    allSum += solveFastestPath(buttons[idx], joltage_req[idx])


e = time.time()
print()
print(f"P2 {allSum} button presses are needed for correct joltages")
print("Time taken: " + str(e - s) + " seconds")
