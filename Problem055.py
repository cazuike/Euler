from collections import defaultdict
import itertools
import math

flips = defaultdict(bool)
lychel = []

for i in range(1,10000):
    if flips[i]:
        continue
    else:
        newint = i
        itr = 0
        arr = []
        while str(newint) != str(newint)[::-1] and itr < 50:
            itr += 1
            newint = int(str(newint)) + int(str(newint)[::-1])
            arr.append(newint)
        if itr == 50:
            lychel.append(i)
        else:
            for a in arr:
                flips[a] = True
print(len(lychel)+3)
