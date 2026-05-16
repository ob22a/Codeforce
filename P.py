def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))

    view = 0

    for i in range(n):
        view+=max(0,min(m-i-1,a[i]))
    
    print(view)

t=int(input())

for _ in range(t):
    solve()