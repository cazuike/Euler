totality = 0
for i in range(2,1000000):
    total = 0
    for j in str(i):
        total += int(j)**5
    if total == i:
        totality += total
print(totality)
