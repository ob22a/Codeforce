def solve():
    n,m=map(int,input().split())
    length = min(n,m)

    print(length**2)

t=int(input())
for _ in range(t):
    solve()