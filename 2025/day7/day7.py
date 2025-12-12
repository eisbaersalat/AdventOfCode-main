import time

with open("day7/input.txt", encoding="utf-8") as file:
    plan = [line.rstrip() for line in file]

s = time.time()

# convert to list of lists of strings
plan = [list(r) for r in plan]
print()


N = len(plan[0])

## ---------------PART 1-----------------
# find start
beam_locations = [False] * N
numSplits = 0
beam_locations[plan[0].index("S")] = 1

# go through each line
for ln in range(1, len(plan)):   

    # check for splitters
    for i in range(N):
        if plan[ln][i] == "^" and beam_locations[i]:

            beam_locations[i-1] = True
            beam_locations[i+1] = True
            numSplits += 1

            beam_locations[i] = False
            
    # plot beams
    for i in range(N):
        if beam_locations[i]:
            plan[ln][i] = "|"


e = time.time()
print()
print(f"P1: Number of Tachyon splits: {numSplits}")
print("Time taken: " + str(e - s) + " seconds")
    

## ---------------PART 2 -----------------
s = time.time()
numPaths = 0
pascals = [ list( [0]*N ) for _ in range(len(plan) )]
pascals[0][plan[0].index("S")] = 1
c_old = 0

for i in range(1, len(plan)):
    for c in range(N):
        
        if plan[i][c] == "|":
            
            # overtake value from above
            if plan[i-1][c] == "|" or plan[i-1][c] == "S":
                tmp = pascals[i-1][c]
            else:
                tmp = 0
            
            # overtake values from splitted pathes left and right
            if c > 0:
                if plan[i][c-1] == "^":
                    tmp += pascals[i-1][c-1]
            if c < (N-1):
                if plan[i][c+1] == "^":
                    tmp += pascals[i-1][c+1]

            pascals[i][c] = tmp


print()
routes = sum(pascals[-1])

e = time.time()
print()
print(f"P2: Number of unique routes: {routes}")
print("Time taken: " + str(e - s) + " seconds")