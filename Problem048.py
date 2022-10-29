from collections import defaultdict
import itertools
import math


last = 0

for i in range(1,1000):
    last += i**i

last = str(last)
print(last[len(last)-10:]) #9110846700
