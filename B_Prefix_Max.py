def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        sol = max(a) * n

        print(sol)

if __name__ == "__main__":
    solve()