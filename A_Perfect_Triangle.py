def solve():
    n = int(input())
    a = list(map(int,input().split()))
    sol = 1e9

    a.sort()
    for i in range(n-3+1):
        sol=min(sol,a[i+2]-a[i])
    
    print(sol)
t = int(input())
for _ in range(t):
    solve()