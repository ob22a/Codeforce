def solve():
    n,c,d = map(int, input().split())
    a = list(map(int, input().split()))

    start = min(a)

    res = []
    for i in range(n):
        for j in range(n):
            res.append(start + i*c + j*d)

    if sorted(res) == sorted(a):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()