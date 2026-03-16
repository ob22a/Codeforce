def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    if n == 1 and m == 1:
        print(-1)
        return

    flat = []
    for row in a:
        flat.extend(row)

    rotated = flat[1:] + flat[:1]
    
    for i in range(n):
        row = rotated[i*m:(i+1)*m]
        print(*row)

t = int(input())
for _ in range(t):
    solve()
