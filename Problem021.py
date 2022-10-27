
from collections import defaultdict

divisors = defaultdict(list)
for i in range(10001):
    for j in range(1,i):
        if i % j == 0:
            divisors[i].append(j)
seen = set()
for k in divisors.keys():
    if sum(divisors[k]) in divisors and sum(divisors[sum(divisors[k])]) == k:
        seen.add(k)
print(sum(seen)) #40284
