import time
import hashlib



s = time.time()
directions = []
input = 'iwrupvqb'

i = 0

while True:
    concatStr = input + str(i)
    hash = hashlib.md5(concatStr.encode())
    if hash.hexdigest()[0:6] == "000000":
        break
    else:
        i += 1

print(f"string {concatStr} results in hash {hash.hexdigest()}")

e = time.time()
print(f"runtime: {e-s} s") 
