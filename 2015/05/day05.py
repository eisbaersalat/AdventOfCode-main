import time

start = time.time()
allStrings = []
with open("2015/05/input.txt", encoding="utf-8") as file:
    for line in file:
        allStrings.append(line.rstrip())


## PART 1
vowels = ['a', 'e', 'i', 'o', 'u']
forbidden = ['ab', 'cd', 'pq', 'xy']


def includesForbiddenString(s):
    for f in forbidden:
        if f in s:
            return 1
    return 0

def countVowels(s):
    nV = 0
    for letter in s:
        if letter in vowels:
            nV += 1
    return nV 

def containsDoubleLetter(s):

    for idx in range(len(s)-1):
        if s[idx] == s[idx+1]:
            return 1
    return 0

sumNiceStrings = 0

for s in allStrings:

    if not includesForbiddenString(s):
        if countVowels(s) >= 3:
            if containsDoubleLetter(s):
                sumNiceStrings += 1

e = time.time()
print(f" there are {sumNiceStrings} nice strings")
print(f"runtime: {e-start} s")      


 ## PART 2

start = time.time() 
sumNiceStrings = 0
def repeatedPair(s):
    for idx in range(len(s)-1):
        pair = s[idx:idx+2]
        tmp = s[idx+2:]

        if pair in tmp:
            return 1

    return 0

def repeatedLetter(s):
    for idx in range(len(s)-2):
        if s[idx] == s[idx+2]:
            return 1
    return 0


for s in allStrings:

    if repeatedPair(s):
        if repeatedLetter(s):
            sumNiceStrings += 1

e = time.time()
print(f" there are {sumNiceStrings} nice strings")
print(f"runtime: {e-start} s")       