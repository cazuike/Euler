from collections import defaultdict
import itertools
import math

limit = 100
notFound = True
while notFound:
    for i in range(limit,2*limit):
        if set(str(i)) == set(str(2*i)) == set(str(3*i)) == set(str(4*i)) == set(str(5*i)) == set(str(6*i)):
            notFound = False
            print(i)
            break
    limit = limit * 10
