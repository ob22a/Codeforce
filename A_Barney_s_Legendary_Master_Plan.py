def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        no_unique = len(set(arr))

        print(2*no_unique - 1)

if __name__ == "__main__":
    solve()