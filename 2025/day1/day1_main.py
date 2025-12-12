import numpy as np
import math

numberofZeros = 0
zeroCrossings = 0

with open("combinations.txt") as file:
    combinations = [line.rstrip() for line in file]
# print(combinations)


def inputRotation(pos, inputStr):
    global numberofZeros, zeroCrossings
    
    oldPos = pos
    # print(inputStr)
    direction = inputStr[0]
    number = int(inputStr[1:])

    zc = 0

    complRotations = abs(number)//100
    zc += complRotations
    remainingRotation = abs(number)%100
    
    if direction == "L":
        pos -= remainingRotation
    else:
        pos += remainingRotation
    
    if pos == 0:
        zc += 1
    elif pos > 99:
        zc += 1
        pos -= 100
    elif pos < 0:
        if oldPos != 0:
            zc += 1
        pos += 100
    
    zeroCrossings += zc

    return pos

pos = 50
for c in combinations:
    pos = inputRotation(pos, c)


print("The final position is " + str(pos) + " \n"
      "the old password is " + str(numberofZeros) + "\n"
      "password to method 0x434C49434B is " + str(zeroCrossings))

