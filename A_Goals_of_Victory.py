def solve():
    n=int(input())
    a=list(map(int,input().split()))

    total = sum(a)

    print(0-total)

t=int(input())
for _ in range(t):
    solve()