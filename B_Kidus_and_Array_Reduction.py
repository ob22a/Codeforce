def solve():
    n=int(input())
    a=list(map(int,input().split()))

    prefix_max=[0]*n
    prefix_max[0]=a[0]
    count=1

    for i in range(1,n):
        if prefix_max[i-1]<=a[i]:
            count+=1

        prefix_max[i]=max(prefix_max[i-1],a[i])

    print(count)
    
t=int(input())

for _ in range(t):
    solve()