isPrime = dict() #modified sieve of eratosthenes :)
isPrime[1] = True
k = 0
i = 1
while i != 2000000:
    if i not in isPrime:
        isPrime[i] = True
        for j in range(2*i,10000000,i):
            isPrime[j] = False
        k += i
    i += 1
print(k)
