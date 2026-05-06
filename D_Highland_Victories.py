def solve():
    n=int(input())
    a=list(map(int,input().split()))

    happy_days=0
    for i in range(1,n):
        if a[i]>a[i-1]:
            happy_days+=1
    
    print(happy_days)

t=int(input())
for _ in range(t):
    solve()