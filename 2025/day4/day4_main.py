import time

neighbors = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

with open("day4/floorplan.txt", encoding="utf-8") as file:
    plan = [line.rstrip() for line in file]

# convert to list of lists of strings
plan = [list(r) for r in plan]

        # x
limits = (0, 0, len(plan)-1, len(plan[0])-1)

def isAccessable(plan, x, y ):
    sumFree = 0
           
    for n in neighbors:
        # outside border => FREE
        if x+n[0]<limits[1] or y+n[1]<limits[0] or x+n[0]>limits[3] or y+n[1]>limits[2]:
            sumFree += 1
        else:
            if plan[y+n[1]][x+n[0]] != "@":
                sumFree += 1

    if sumFree > 4:
        return True
    else: 
        return False


s = time.time()
accessablePaperrols = 0
freeRollFound = True

while freeRollFound:
    freeRollFound = False
    for r in range( len(plan) ):
        for c in range( len(plan[0]) ):
        
            if plan[r][c] == "@":
                if isAccessable(plan, c, r):
                    accessablePaperrols += 1
                    freeRollFound = True
                    plan[r][c] = "x"


e = time.time()

print("There are " + str(accessablePaperrols) + " accessable paper rolls")
print()
# for p in plan:
#     print(p)
# print()
print("freeRollFound is " + str(freeRollFound))
print("Time taken: " + str(e - s) + " seconds")