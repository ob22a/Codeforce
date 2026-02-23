from collections import defaultdict

def solve():
    n = int(input())
    ravenCount = defaultdict(int)
    total = 0

    for _ in range(n):
        m = int(input())
        for _ in range(m):
            raven, hour = input().split()
            ravenCount[(raven, hour)] += 1
        total+=1

    for count in ravenCount.values():
        if count / total >= 0.8:
            print("YES")
            return

    print("NO")

solve()