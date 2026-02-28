def solve():
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]

    a.sort(key=lambda a: a[0]+a[1])
    
    for arr in a:
        print(*arr,end=" ")
    print()
t = int(input())
for _ in range(t):
    solve()