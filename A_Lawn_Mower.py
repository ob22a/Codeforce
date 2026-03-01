def solve():
    n,w=map(int,input().split())
    groups = n//w
    print(n-groups)

t = int(input())
for _ in range(t):
    solve()