def solve():
    n=int(input())
    sol=0
    
    for i in range(n):
        a,b=map(int,input().split())
        if a>b:
            sol+=1
    
    print(sol)

t=int(input())

for _ in range(t):
    solve()