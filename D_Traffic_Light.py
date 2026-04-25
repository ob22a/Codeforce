def solve():
    n,c=input().split()
    n=int(n)
    
    s=input()
    if c=='g':
        print(0)
        return

    last_g=-1
    sol=0

    s+=s

    for i in range(2*n-1,-1,-1):
        if s[i]=='g':
            last_g=i
        if s[i]==c and last_g!=-1:
            sol=max(sol,last_g-i)
    
    print(sol)


t=int(input())
for _ in range(t):
    solve()