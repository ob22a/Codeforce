def findMex(a):
    s = {x for x in a if x >= 0}
    mex = 0
    while mex in s:
        mex += 1
    return mex


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    best = 0
    for val in a:
        x = -val
        shifted = [num + x for num in a]
        best = max(best, findMex(shifted))
    
    print(best)


t = int(input())
for _ in range(t):
    solve()