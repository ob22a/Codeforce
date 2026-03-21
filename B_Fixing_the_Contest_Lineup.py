def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    shift = 0
    idx = 0

    while idx<n and shift<n-idx:
        if a[idx]>b[idx+shift]:
            shift+=1
            continue
            
        idx+=1

    print(shift)

t = int(input())
for _ in range(t):
    solve()