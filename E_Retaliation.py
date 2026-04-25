def solve():
    n=int(input())
    a=list(map(int,input().split()))

    b=(2*a[0]-a[1])//(n+1) # removing size-index+1
    c=b-a[0]+a[1] # removing index

    if b<0 or c<0:
        print("NO")
        return

    for i in range(n):
        a[i]-=c*(i+1)
        a[i]-=b*(n-i)

    for i in range(n):
        if a[i]!=0:
            print("NO")
            return
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()