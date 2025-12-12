import time

fresh_ranges = []
ingredients  = []

with open("day5/db.txt", encoding="utf-8") as file:
    for _line in file:
        _line = _line.rstrip()
        if "-" in _line:
            (id1, id2) = _line.split("-")
            fresh_ranges.append((int(id1), int(id2)))
        elif _line == "":
            pass
        else:
            ingredients.append(int(_line))


def isFresh(id):
    global fresh_ranges
    for rng in fresh_ranges:
        if id >= rng[0] and id <= rng[1]:
            return True
        
    return False

def checkOverlap(rng1, rng2):

    # no overlap
    if rng1[1] < rng2[0]:
        return False, None
    elif rng2[1] < rng1[0]:
        return False, None
    else:
        # combine both ranges 
        rngNew = (min(rng1[0], rng2[0]), max(rng1[1], rng2[1]))
        return True, rngNew

s = time.time()

# part 1
numFreshIngredients = 0
for ing in ingredients:
    if isFresh(ing):
        numFreshIngredients += 1


# part 2

thereAreOverlaps = True
numRanges = len(fresh_ranges)
deleted = [False] * numRanges
iterCount = 1

while thereAreOverlaps:

    print('Iteration ' + str(iterCount))
    iterCount += 1
    thereAreOverlaps = False

    # compare each range against each
    for idx1 in range(0, numRanges-1):
        if not deleted[idx1]:
            for idx2 in range(idx1+1, numRanges):
                if not deleted[idx2]:
                    isOverlap, newRng = checkOverlap(fresh_ranges[idx1], fresh_ranges[idx2])
                    if isOverlap:
                        thereAreOverlaps = True
                        # keep new combined range in idx1 and delete idx2 
                        fresh_ranges[idx1] = newRng
                        deleted[idx2] = True


# sum over all not deleted ranges
numFreshIds = 0
for idx in range(0, numRanges):
    if not deleted[idx]:
        numFreshIds += (fresh_ranges[idx][1] - fresh_ranges[idx][0] + 1)

e = time.time()

print("P1: There are " + str(numFreshIngredients) + " fresh ingredients")
print("P2: There are " + str(numFreshIds) + " Ids which are fresh ")
print()
print("Time taken: " + str(e - s) + " seconds")