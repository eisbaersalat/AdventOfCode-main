import time
import math
import tkinter
import shapely

with open("day9/input.txt", encoding="utf-8") as file:
    coords = [list(map(int,line.rstrip().split(',') )) for line in file]

shapelyPoly = shapely.geometry.Polygon(coords)


def isOverlapping(c1, c2):
    rect = shapely.geometry.Polygon([(c1[0], c1[1]), (c1[0],c2[1]), (c2[0],c2[1]), (c2[0],c1[1])])
    if rect.overlaps(shapelyPoly):
        return True
    else:
        return False

def computeArea(c1, c2):
    return (max(c1[0], c2[0])-min(c1[0], c2[0]) + 1) * (max(c1[1], c2[1])-min(c1[1], c2[1]) + 1) 


## ---------------PART 1 -----------------
s = time.time()

largestRectangle = (0, [0,0], [0,0])

for idx1 in range(len(coords) - 1):
    for idx2 in range(idx1+1, len(coords)):

        r = computeArea(coords[idx1], coords[idx2])

        if r > largestRectangle[0]:
            largestRectangle = (r, coords[idx1], coords[idx2])

e = time.time()
print()
print(f"P1: Largest Rectangle has an area of {largestRectangle[0]} with points {largestRectangle[1]} and {largestRectangle[2]}")
print("Time taken: " + str(e - s) + " seconds")

## ---------------PART 2 -----------------
s = time.time()

allRectangles = []

for idx1 in range(len(coords) - 1):
    for idx2 in range(idx1+1, len(coords)):

        r = computeArea(coords[idx1], coords[idx2])

        allRectangles.append((r, coords[idx1], coords[idx2]))

# sort descending
allRectangles.sort(key=lambda x: x[0], reverse=True)

# check if any line is crossing the polygon
kk = 0
for r in allRectangles:
    kk += 1
    if not isOverlapping(r[1], r[2]):
        break

e = time.time()
print()
print(f"P2: Largest Rectangle has an area of {r[0]} with points {r[1]} and {r[2]}")
print("Time taken: " + str(e - s) + " seconds")

# plot shape
if True:
    win = tkinter.Tk()
    win.geometry("1000x1000")
    canvas = tkinter.Canvas(win, width=900, height=900, background="yellow")
    canvas.grid()

    xf = 900/100000
    yf = 900/100000

    for i in range(len(coords) - 1):
        canvas.create_line(coords[i][0]*xf, coords[i][1]*yf, coords[i+1][0]*xf, coords[i+1][1]*yf)

    canvas.create_line(coords[-1][0]*xf, coords[-1][1]*yf, coords[0][0]*xf, coords[0][1]*yf)

    # plot largest rectangle (P2)
    canvas.create_line(r[1][0]*xf, r[1][1]*yf, r[1][0]*xf, r[2][1]*yf, r[2][0]*xf, r[2][1]*yf, r[2][0]*xf, r[1][1]*yf, r[1][0]*xf, r[1][1]*yf, fill="red") 

    win.mainloop()