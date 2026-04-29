def solve():
    n=int(input())
    a=list(map(int,input().split()))

    smallest = min(a)
    if a[0]!=smallest:
        print("NO")
    else:
        print("YES")

t=int(input())
for _ in range(t):
    solve()