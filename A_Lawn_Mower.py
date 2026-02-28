def solve():
    n,w=map(int,input().split())
    i=0
    sol=0
    while i<n:
        sol+=min(w-1,n-i)
        i+=w
    print(sol)

t = int(input())
for _ in range(t):
    solve()