def solve():
    n,A,B = map(int,input().split())
    s=list(map(int,input().split()))

    total=sum(s)
    b = sorted(s[1:])

    i=len(b)-1
    blocked = 0

    while i>=0 and s[0]*A/total<B:
        total-=b[i]
        i-=1
        blocked+=1
    
    print(blocked)

solve()