isPrime = dict()
primes = []
isPrime[1] = True
for i in range(2,1000000): #sieve of eratosthenes
    if i not in isPrime:
        isPrime[i] = True
        primes.append(i)
        for j in range(2*i,1000000,i):
            isPrime[j] = False
circle = set()
for p in primes:
    string = str(p)
    circ = True
    for j in range(len(string)-1):
        if not isPrime[int(string[j+1:]+string[:j+1])]:
            circ =  False
    if circ:
        circle.add(p)
print(len(circle)) #55
