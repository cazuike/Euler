from collections import defaultdict
import itertools
import math

isPrime = dict()
primes = []
isPrime[1] = True
for i in range(2,1000000000): #sieve of eratosthenes
    if i not in isPrime:
        isPrime[i] = True
        primes.append(i)
        for j in range(2*i,1000000000,i):
            isPrime[j] = False

primes = 0
total = 1


for i in itertools.count(3,2):
    total += 4
    if isPrime[i**2]:
        primes += 1
    if isPrime[i**2 -(i-1)]:
        primes += 1
    if isPrime[i**2 -2*(i-1)]:
        primes += 1
    if isPrime[i**2 -3*(i-1)]:
        primes += 1
    if primes/total < 0.1:
        print(i)
        break
