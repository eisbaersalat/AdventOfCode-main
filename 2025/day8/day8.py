import time
import math

with open("day8/input.txt", encoding="utf-8") as file:
    boxes = [list(map(int, line.rstrip().split(',') )) for line in file]

def computeDistance(n1, n2):
    return math.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2 + (n1[2]-n2[2])**2)


def isNodeIngroup(idx):
    for i,c in enumerate(connections):
        if idx in c:
            return True, i
    
    return False, None


## ---------------PART 1 -----------------
# s = time.time()

# # to save groups of connections
# connections = []
# distances = []

# # compute distance between all nodes and sort them
# for idx1 in range(0, len(boxes)-1):
#     for idx2 in range(idx1+1, len(boxes)):
#         d = computeDistance(boxes[idx1], boxes[idx2])
#         distances.append( (d, idx1, idx2) )

# distances.sort(key=lambda x: x[0])
# print()

# for _kk in range(0, 1000):
#     x = distances[0]
#     s1 = x[1]
#     s2 = x[2]

#     idx1InGroup, id1 = isNodeIngroup(s1)
#     idx2InGroup, id2 = isNodeIngroup(s2)

#     if idx1InGroup and idx2InGroup:
#         if id1 == id2:
#             pass
#         else:
#             # merge both connection cluster
#             connections[id1] = connections[id1] + connections[id2]
#             connections.pop(id2)

#     elif idx1InGroup:
#         connections[id1].append(s2)
#     elif idx2InGroup:
#         connections[id2].append(s1) 
#     else:
#         connections.append([s1, s2])

#     distances.pop(0)
    
    

# L = [len(c) for c in connections]
# sortIdx = sorted(range(len(L)), key=lambda k:L[k], reverse=True)
# L_sorted = [L[c] for c in sortIdx]
# connSorted = [connections[c] for c in sortIdx]
# prod3 = L_sorted[0]*L_sorted[1]*L_sorted[2]

# e = time.time()
# print()
# print(f"P1: Result is: {prod3}")
# print("Time taken: " + str(e - s) + " seconds")
    

## ---------------PART 2 -----------------
s = time.time()

# to save groups of connections
connections = []
distances = []

# compute distance between all nodes and sort them
for idx1 in range(0, len(boxes)-1):
    for idx2 in range(idx1+1, len(boxes)):
        d = computeDistance(boxes[idx1], boxes[idx2])
        # add the x coordinates of both points to the tuple for final calculation 
        distances.append( (d, idx1, idx2, boxes[idx1][0], boxes[idx2][0]) )

distances.sort(key=lambda x: x[0])


while True:
    x = distances[0]
    s1 = x[1]
    s2 = x[2]

    idx1InGroup, id1 = isNodeIngroup(s1)
    idx2InGroup, id2 = isNodeIngroup(s2)

    if idx1InGroup and idx2InGroup:
        if id1 == id2:
            pass
        else:
            # merge both connection cluster
            connections[id1] = connections[id1] + connections[id2]
            connections.pop(id2)

    elif idx1InGroup:
        connections[id1].append(s2)
    elif idx2InGroup:
        connections[id2].append(s1) 
    else:
        connections.append([s1, s2])

    # check if all elements are in largest group
    connections.sort(key= lambda x: len(x))

    if len(connections[0]) == len(boxes):
        break
    else:
        distances.pop(0)


e = time.time()
print()
print(f"P2: Result is: {distances[0][3] * distances[0][4]}")
print("Time taken: " + str(e - s) + " seconds")