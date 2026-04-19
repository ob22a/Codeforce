def solve():
    n=int(input())
    a = list(map(int,input().split()))

    sol = 0
    i=0
    
    while i<n and a[i]==0:
        i+=1
    
    for idx in range(i,n-1):
        sol+=a[idx]
        if a[idx]==0:
            sol+=1
        
    print(sol)

t = int(input())

for _ in range(t):
    solve()