import time

test = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

with open("day3/joltInput.txt") as file:
    allBanks = [line.rstrip() for line in file]

def getHighestJoltage2(bank: str) -> int:
    n1 = n2 = 0
    idx1 = None

    # get highest first digit in (0, len-1)
    for idx in range(len(bank)-1):
      
        if int(bank[idx]) > n1:
            n1 = int(bank[idx])
            idx1 = idx

    # get highest second digit in (idx1+1, end)
    for idx in range(idx1+1, len(bank)):
        if int(bank[idx]) > n2:
            n2 = int(bank[idx]) 

    return n1*10 + n2


def getHighestJoltage12(bank: str) -> int:
    numberDigits = 12
    outputList = [0] * 12
    idxStart = -1

    for dig in range(numberDigits):

        for idx in range(idxStart+1, len(bank)-numberDigits+dig+1):
        
            if int(bank[idx]) > outputList[dig]:
                outputList[dig] = int(bank[idx])
                idxStart = idx

    # convert list of ints -> list of str -> str -> int
    delim = ""
    listStr = map(str, outputList)
    string = delim.join(listStr)

    return int(string)


summedJolts = 0

s = time.time()

for bank in allBanks:
    jolt = getHighestJoltage12(bank)
    summedJolts += jolt
    print(jolt)

e = time.time()

print("The overall max Jolt is: " + str(summedJolts))
print("Time taken: " + str(e - s) + " seconds")