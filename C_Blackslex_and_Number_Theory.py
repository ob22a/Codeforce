def solve():
    n = int(input())    
    a = list(map(int,input().split()))

    smallest=float('inf')
    second_smallest=float('inf')
    for i in range(n):
        if a[i]<smallest:
            second_smallest=smallest
            smallest=a[i]
        elif a[i]<second_smallest:
            second_smallest=a[i]
    print(max(smallest,second_smallest-smallest))

t = int(input())
for _ in range(t):
    solve()