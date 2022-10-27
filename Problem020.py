memo = {}

def factorial(n): #memoization
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorial(n-1)
    return memo[n]

items = list(str(factorial(100)))

total = 0
for i in items:
    total += int(i)
print(total) #648
