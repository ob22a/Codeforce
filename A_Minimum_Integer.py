import math

def solve():
    l,r,d=map(int,input().split())
    ans = d
    if l/d<=1:
        ans = (math.floor(r/d)+1)*d
    
    print(ans)

q = int(input())
for _ in range(q):
    solve()