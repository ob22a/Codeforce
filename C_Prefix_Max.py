def solve():
    n=int(input())
    a=list(map(int,input().split()))

    largest = max(a)
    idx = n-1-a[::-1].index(largest)

    a[0],a[idx]=a[idx],a[0]


    max_ = 0
    sol = 0
    for num in a:
        max_=max(max_,num)
        sol+=max_
    
    print(sol)

t=int(input())

for _ in range(t):
    solve()