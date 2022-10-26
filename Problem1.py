total = 0
for i in range(1000): #last number is exclusive so +1 to include 10000
    if i % 3 == 0 or i % 5 ==0 :
        total += i
print(total)
