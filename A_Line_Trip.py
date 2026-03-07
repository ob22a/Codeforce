def solve():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))

    sol=a[0]
    for i in range(n-1):
        sol=max(sol,a[i+1]-a[i])
    
    sol=max(sol,(x-a[-1])*2)

    print(sol)

t = int(input())
for _ in range(t):
    solve()