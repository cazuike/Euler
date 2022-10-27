#could use a hash table to memorize prior calculations to reduce run time!
k = 0
num = None
for i in range(1,1000000):
    di = i
    z = 0
    while di != 1:
        if di % 2 == 0:
            di = di // 2
        else:
            di = 3*di+1
        z += 1
    if z > k:
        k = z
        num = i
print(k)
#brute force answer 837799
