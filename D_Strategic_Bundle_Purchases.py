def solve():
    n,k = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a.sort(reverse=True)
    b.sort()

    cost = sum(a)
    index=0
    
    for i in range(k):
        discounted_idx = index+b[i]-1
        if discounted_idx<n:
            cost-=a[discounted_idx]
            index=discounted_idx+1
    
    print(cost)
    
t = int(input())
for _ in range(t):
    solve()