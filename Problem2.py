back = 1 #every 3rd number of fib sequence is even , odd + even + even -> even
front = 2
total = 2
while front <= 4000000:
    temp = front+back
    back = front
    front = temp
    if temp % 2 == 0:
        total += temp
print(total)
