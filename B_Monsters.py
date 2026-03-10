def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    b = [(-(a[i] % k) if (a[i]%k!=0) else -k,i+1) for i in range(n)]
    b.sort()

    print(*[idx for _,idx in b])

t = int(input())
for _ in range(t):
    solve()