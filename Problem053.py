def factorial(n): #memoization
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorial(n-1)
    return memo[n]


total = 0
for n in range(1,100):
    for r in range(1,n):
            if factorial(n)/(factorial(r)*factorial(n-r)) >= 1000000:
                total += 1
print(total)
        
