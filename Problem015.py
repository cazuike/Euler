count = [0]
def dp(x,y): #unoptimizied dynamic programming
    if x == y == 0:
        count[0] += 1
    if x < 0 or y < 0:
        return
    dp(x-1,y)
    dp(x,y-1)

memo = {}
def optimal(x,y): #uses memoization <- way better solution !!
    if (x,y) in memo:
        return memo[(x,y)]
    if x == y == 0:
        return 1
    if x < 0 or y< 0:
        return 0
    memo[(x,y)] = optimal(x-1,y) + optimal(x,y-1)
    return memo[(x,y)]
print(optimal(20,20))
