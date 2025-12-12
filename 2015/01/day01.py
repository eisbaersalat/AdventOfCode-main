import time

s = time.time()

with open("2015/01/input.txt", encoding="utf-8") as file:
    instructions = file.read()

## PART 1
floor = 0

for i,l in enumerate(instructions):
    if l == "(":
        floor += 1
    elif l == ")":
        floor -= 1

e = time.time()

print(f"go to floor {floor}")
print(f"runtime: {e-s} s")      


 ## PART 2
floor = 0

for i,l in enumerate(instructions):
    if l == "(":
        floor += 1
    elif l == ")":
        floor -= 1

    if floor < 0:
        break

e = time.time()

print(f"to basement after instruction {floor}")
print(f"runtime: {e-s} s")    