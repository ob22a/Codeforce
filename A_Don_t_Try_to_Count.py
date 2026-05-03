def isSubset(x,s):
    lx=len(x)
    ls=len(s)

    if lx<ls:
        return False
    
    for i in range(lx-ls+1):
        if x[i:i+ls]==s:
            return True
    
    return False

def solve():
    n,m=map(int,input().split())
    x=input()
    s=input()

    sol=0

    for sol in range(6):
        if isSubset(x,s):
            print(sol)
            return
        
        x+=x
    print(-1)
    

t=int(input())
for _ in range(t):
    solve()