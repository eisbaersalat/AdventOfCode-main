import time
import math
import itertools
import numpy as np

area_sizes = []
numObj = []

with open("day12/input.txt", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        if bool(line):
            if "x" in line:
                area, numbers = line.split(": ")
                area = area.split("x")
                area_sizes.append(int(area[0]) * int(area[1]))

                numbers = numbers.split(" ")
                numObj.append(  sum(list(map(int, numbers))) )




## ---------------PART 1 -----------------
s = time.time()

def checkFit(area_size, numObjects):
    if numObjects*9 <= area_size:
        return True
    else:
        return False
    
numFitting = 0    
for i in range(len(area_sizes)):
    numFitting += checkFit(area_sizes[i], numObj[i])




e = time.time()
print()
print(f"P1: {numFitting} of the area are large enough")
print("Time taken: " + str(e - s) + " seconds")

## ---------------PART 2 -----------------
# s = time.time()

# allSum = 0

# for idx in range(len(joltage_req)):
#     allSum += solveFastestPath(buttons[idx], joltage_req[idx])


# e = time.time()
# print()
# print(f"P2 {allSum} button presses are needed for correct joltages")
# print("Time taken: " + str(e - s) + " seconds")
