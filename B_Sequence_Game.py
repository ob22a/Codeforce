def solve():
    n=int(input())
    a=list(map(int,input().split()))
    
    sol=[a[0]]

    for i in range(1,n):
        if a[i]>=a[i-1]:
            sol.append(a[i])
        else:
            sol.append(a[i])
            sol.append(a[i])
    
    print(len(sol))
    print(*sol)

t=int(input())
for _ in range(t):
    solve()