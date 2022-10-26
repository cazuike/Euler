#sum of numbers 1 to n can be expressed as product of strict primes
isPrime = dict()
isPrime[1] = True
for i in range(2,21): #sieve of eratosthenes
    if i not in isPrime:
        isPrime[i] = True
        for j in range(2*i,21,i):
            isPrime[j] = False
answer = 1
#uses problem 3 to solve - if min and max prime factor != then its not a nth root
def maxPrime(number): # only true if n > 2
    counter = 2
    while number != 1:
        if number % counter == 0:
            number = number // counter
        else:
            counter += 1
    return counter
def minPrime(number): # only true if n > 2
    counter = 2
    while number != 1:
        if number % counter == 0:
            return counter
        else:
            counter += 1
    return counter
for k in range(1,21):
    if isPrime[k]:
        answer = answer * k
    else:
        if minPrime(k) == maxPrime(k):
            answer = answer * minPrime(k)
