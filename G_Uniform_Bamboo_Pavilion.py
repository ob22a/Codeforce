from math import lcm

def solve():
    n=int(input())
    l=list(map(int,input().split()))
    c=list(map(int,input().split()))

    intersection = 1
    for h in l:
        intersection=lcm(intersection,h)
    
    if(any(l[i]*c[i]<intersection for i in range(n))):
        print(-1)
        return 

    sol=[]
    for i in range(n):
        sol.append(intersection//l[i])
    
    print(intersection)
    print(*sol)

t=int(input())
for _ in range(t):
    solve()