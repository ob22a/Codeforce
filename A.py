def solve():
    n,k,b=map(int,input().split())
    c=list(map(int,input().split()))

    c.sort()
    
    free=0
    amount = 0
    total = 0

    for coin in c:
        if coin<=k:
            total+=1
            amount+=1
            k-=coin

        if amount==b:
            free+=1
            amount=0
    
    print(min(n,free+total))

t=int(input())

for _ in range(t):
    solve()