def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    a.sort()
    ans = -1
    
    for i in range(n-2,-1,-1):
        if a[n-1]-a[i]>=k:
            ans=max(ans,a[n-1]*a[i])
    
    print(ans)

t=int(input())

for _ in range(t):
    solve()