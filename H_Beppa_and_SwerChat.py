def solve():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    idx_a={a[i]:i for i in range(n)}
    offline = 0
    last_online = n

    for i in range(n-1,-1,-1):
        if last_online>idx_a[b[i]]:
            offline+=1
            last_online=idx_a[b[i]]
        else:
            break

    print(n-offline)

t = int(input())
for _ in range(t):
    solve()