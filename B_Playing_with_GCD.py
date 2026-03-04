import math

def solve():
    n = int(input())
    a = list(map(int,input().split()))

    '''
        a1 = gcd(b1,b2) a2 =gcd(b2,b3) ... an=gcd(bi,bi+1)
        a1 being a gcd of the two mean that b1 and b2 are its multiple and for
        a2 b2 and b3 are its multiple 

        here b1 is a multiple of a1
            b2 is a multiple of a1 and a2
            b3 is a multiple of a2  and a3
            ...
            bn is a multiple of an-1 and an
            bn+1 is a multiple of only an
    '''

    b = [0]*(n+1)
    b[0]=a[0]
    b[n]=a[n-1]

    for i in range(1,n):
        b[i]=math.lcm(a[i-1],a[i])
    
    for i in range(n):
        if a[i]!=math.gcd(b[i],b[i+1]):
            print("NO")
            return
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()