seen = set()
for i in range(2,101):
    for j in range(2,101):
        seen.add(i**j)
print(len(seen))
