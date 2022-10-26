high = 0 #bruteforce
for i in range(100,1000):
    for j in range(100,1000):
        string = str(i*j)
        if string[:len(string)//2] == string[len(string)//2:][::-1]:
            high = max(high,i*j)
print(high)
