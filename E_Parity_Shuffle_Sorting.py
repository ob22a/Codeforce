def solve():
    n=int(input())
    a=list(map(int,input().split()))

    # Easiest way to achieve this is to make all equal so start from the edge and then try to make all values equal to that
    if n == 1:
        print(0)
        return
    
    print(n-1)
    
    if (a[0]+a[-1])%2:
        a[-1]=a[0]
    else:
        a[0]=a[-1]
    
    print(1,n)

    for i in range(1,n-1):
        if (a[0]+a[i])%2:
            a[i]=a[0]
            print(1,i+1)
        else:
            a[i]=a[-1]
            print(i+1,n)

t = int(input())
for _ in range(t):
    solve()