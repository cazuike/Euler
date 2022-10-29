from collections import defaultdict
import itertools
import math

isPrime = dict()
primes = []
isPrime[1] = True
for i in range(2,10000): #sieve of eratosthenes
    if i not in isPrime:
        isPrime[i] = True
        primes.append(i)
        for j in range(2*i,10000,i):
            isPrime[j] = False
composites = [i for i in isPrime.keys() if (isPrime[i] == False and i % 2 == 1)]
squares = [i**2 for i in range(1,100)]

mini = set()
for c in composites:
    mini.add(c)
    for i in range(len(squares)):
        if c - 2*squares[i] <= 0:
            break
        if isPrime[c - 2*squares[i]]:
            mini.remove(c)
            break
print(mini) #contains elements that violate conjecture with 5777 being first one
