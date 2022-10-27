def factors(n): #long runtime :()
    num = 1
    for i in range(1,n):
        if n % i == 0:
            num += 1
    return num
def summa(n):
    return (n)*(n+1) // 2
count = 1
triangle = summa(count)
while factors(triangle) < 500:
    count += 1
    triangle = summa(count)
print(triangle)
