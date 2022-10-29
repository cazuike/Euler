from collections import defaultdict
import itertools
import math


total = [0]
limit = 30

def backtracking(tot=0,arr = [i for i in range(1,limit)]):
    if tot == limit:
        total[0] += 1
    elif tot > limit:
        return
    for i in range(len(arr)):
        backtracking(tot+arr[i],arr[i:])

backtracking()
print(total)
