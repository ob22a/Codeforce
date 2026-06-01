from collections import defaultdict

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

val = [defaultdict(int) for _ in range(n)]
ans = 0

def dfs(x, y, cnt, limit, v, d):
    global ans

    cur = v ^ a[x][y]

    if cnt == limit:
        if d == 1:
            val[x][cur] += 1
        else:
            ans += val[x][v]
        return

    if 0 <= x + d < n:
        dfs(x + d, y, cnt + 1, limit, cur, d)

    if 0 <= y + d < m:
        dfs(x, y + d, cnt + 1, limit, cur, d)

leftcnt = (n + m - 2) // 2
rightcnt = (n + m - 2) - leftcnt

dfs(0, 0, 0, leftcnt, 0, 1)
dfs(n - 1, m - 1, 0, rightcnt, k, -1)

print(ans)