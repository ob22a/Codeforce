import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a = list(map(int,input().split()))
    s = input().rstrip()

    operation = []
    l,r=0,n-1

    for c in s:
        if c=="L":
            operation.append(l)
            l+=1
        else:
            operation.append(r)
            r-=1
    
    prod = 1
    sol=[]
    
    for i in range(n-1,-1,-1):
        idx = operation[i]
        prod = (prod*a[idx])%m
        sol.append(prod)
    

    print(*sol[::-1])