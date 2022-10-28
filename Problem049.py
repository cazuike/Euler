isPrime = dict()
primes = []
isPrime[1] = True
for i in range(2,10000): #sieve of eratosthenes
    if i not in isPrime:
        isPrime[i] = True
        primes.append(i)
        for j in range(2*i,10000,i):
            isPrime[j] = False
for k in range(7600,10000):
    if k == 8147:
        continue
    if isPrime[k] and isPrime[k-3330] and isPrime[k-6660] and sorted(str(k)) == sorted(str(k-3330)) == sorted(str(k-6660)):
        print(str(k-6660)+str(k-3330)+str(k))
