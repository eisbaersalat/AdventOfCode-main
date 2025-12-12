import time

s = time.time()
presents = []
with open("2015/02/input.txt", encoding="utf-8") as file:
    for line in file:
        presents.append(list(map(int,line.rstrip().split("x"))))

def reqPaper(l, w, h):
    sides = sorted([l,w,h])
    return 2*l*w + 2*w*h + 2*h*l + sides[0]*sides[1]

def reqRibbon(l, w, h):
    sides = sorted([l,w,h])
    return 2*sides[0]+2*sides[1] + w*l*h

## PART 1
total = 0

for p in presents:
    total += reqPaper(p[0], p[1], p[2])

e = time.time()

print(f" {total} square feet are needed")
print(f"runtime: {e-s} s")      


 ## PART 2

s = time.time() 
total = 0

for p in presents:
    total += reqRibbon(p[0], p[1], p[2])

e = time.time()
print(f" {total} feet rinbbon are needed")
print(f"runtime: {e-s} s")      