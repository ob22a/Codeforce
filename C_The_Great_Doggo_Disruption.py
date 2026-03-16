def solve():
    n = int(input())
    s = input().strip()
    from collections import Counter

    cnt = Counter(s)

    if n == 1 or any(v >= 2 for v in cnt.values()):
        print("Yes")
    else:
        print("No")

solve()