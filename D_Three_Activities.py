def solve():
    n = int(input())
    abc = [list(map(int,input().split())) for _ in range(3)]
    K = 5
    import heapq

    top0 = heapq.nlargest(K, enumerate(abc[0]), key=lambda x: x[1])
    top1 = heapq.nlargest(K, enumerate(abc[1]), key=lambda x: x[1])
    top2 = heapq.nlargest(K, enumerate(abc[2]), key=lambda x: x[1])

    ans = 0

    for i, v0 in top0:
        for j, v1 in top1:
            for k, v2 in top2:
                if len({i, j, k}) == 3:
                    ans = max(ans, v0 + v1 + v2)

    print(ans)

t = int(input())
for _ in range(t):
    solve()