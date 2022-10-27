back = 1 #every 3rd number of fib sequence is even , odd + even + even -> even
front = 2
total = 2
while len(str(front)) < 1000:
    temp = front+back
    back = front
    front = temp
print(front)
