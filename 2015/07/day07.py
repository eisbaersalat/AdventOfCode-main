import time
import matplotlib.pyplot as plt

start = time.time()
outputs = []
inputs = []

with open("2015/07/input.txt", encoding="utf-8") as file:
    for line in file:
        s, t = line.rstrip().split(" -> ")
        outputs.append(t)
        inputs.append(s.split(" "))

memory = dict()


## PART 1
def computeInput(node):

    idx = outputs.index(node)
    src = inputs[idx]

    if node in memory:
        return memory[node]
    else:

        if len(src) == 1:
            if src[0].isdigit():
                return int(src[0])
            else:
                memory[node] = computeInput(src[0])
            
        if len(src) == 2:
            if src[1].isdigit():
                return ~int(src[0])
            else:
                memory[node] = ~computeInput(src[1])
            
        if len(src) == 3:
            if src[0].isdigit():
                n1 = int(src[0])
            else:
                n1 = computeInput(src[0])
            if src[2].isdigit():
                n2 = int(src[2])
            else:
                n2 = computeInput(src[2])
            if src[1] == "AND":
                memory[node] = n1 & n2
            elif src[1] == "OR":
                memory[node] = n1 | n2
            elif src[1] == "LSHIFT":
                memory[node] = n1 << n2
            elif src[1] == "RSHIFT":
                memory[node] = n1 >> n2
        
        return memory[node]
            
        

result = computeInput("a") 

e = time.time()
print(f" node a has signal {result} on the wire")
print(f"runtime: {e-start} s")      


 ## PART 2

start = time.time()
outputs = []
inputs = []

with open("2015/07/inputP2.txt", encoding="utf-8") as file:
    for line in file:
        s, t = line.rstrip().split(" -> ")
        outputs.append(t)
        inputs.append(s.split(" "))

memory = dict()

result = computeInput("a") 

e = time.time()
print(f" node a has signal {result} on the wire")
print(f"runtime: {e-start} s")     
print(memory)     