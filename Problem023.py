LIMIT = 28124
divisorsum = [0] * LIMIT
for i in range(1, LIMIT):
	for j in range(i * 2, LIMIT, i):
		divisorsum[j] += i
abundance = [i for (i,x) in enumerate(divisorsum) if x > i]

expressions = [False]*LIMIT

for i in abundance:
    for j in abundance:
        if i + j < LIMIT:
            expressions[i+j] = True
print(sum([i for (i,x) in enumerate(expressions) if not x]))
