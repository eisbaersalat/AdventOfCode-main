import numpy as np
import time
import functools

outputs = []
inputs = []

with open("day11/input.txt", encoding="utf-8") as file:
    for line in file:
        outDev, inDevs = line.split(": ")
        outputs.append(outDev.lstrip().rstrip())
        inputs.append(inDevs.rstrip().split(" "))

sumRoutes = 0
funcCalls = 0

def findAllRoutes(node):
    
    global funcCalls, sumRoutes
    funcCalls += 1

    if inputs[node][0] == "out":
        sumRoutes += 1
        return 1
    
    # get over all inputs which current output node is connected to
    for ins in inputs[node]:
        outNode = [idx for idx in range(len(outputs)) if outputs[idx] == ins][0]
        findAllRoutes(outNode)
    

startNode = [idx for idx in range(len(outputs)) if outputs[idx] == "you"][0]

s = time.time()
findAllRoutes(startNode)
e = time.time()

print(f"number of possible routes: {sumRoutes}")
print(f"number of function calls {funcCalls}")
print(f"needed time {e-s} s")



## ---------------- part 2---------------
import networkx as nx

outputs = []
inputs = []


with open("day11/input.txt", encoding="utf-8") as file:
    for line in file:
        outDev, inDevs = line.split(": ")
        outputs.append(outDev.lstrip().rstrip())
        inputs.append(inDevs.rstrip().split(" "))


def findAllRoutesWithCache(start, target, midpoints):

    lu_table = dict(zip(outputs, inputs))

    @functools.cache
    def count(start, target, midpoints):
        midpoints -= {start}
        if start == target:
            return (1 if not midpoints else 0)
        else:
            sumOverAll = 0
            for ins in lu_table[start]:
                sumOverAll += count(ins, target, midpoints)
            return sumOverAll

    return count(start, target, midpoints)


s = time.time()

result = findAllRoutesWithCache("svr", "out", frozenset({"dac", "fft"}))

print(result)


e = time.time()
print(f"needed time {e-s} s")
