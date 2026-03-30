def solve():
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())

    if x2 == y2:
        print("NO")
        return

    if (x1 - y1) * (x2 - y2) < 0:
        print("NO")
        return

    print("YES")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()