def solve():
    n = int(input())
    v = list(map(int, input().split()))
    
    if n == 1:
        print(-1)
        return
    
    i = 0

    while i < n:
        j = i
        while i < n and j < n and v[i] == v[j]:
            j += 1
        if j - i == 1:
            print(-1)
            return
        i = j
    
    i = 0
    res = []
    while i < n:
        j = i
        while i < n and j < n and v[i] == v[j]:
            j += 1

        for k in range(i + 1, j):
            res.append(k + 1)  
        res.append(i + 1)
        i = j
    
    print(*res)

t = int(input())
for _ in range(t):
    solve()
