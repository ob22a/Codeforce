def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        mini = max(arr[0], arr[1])
        for i in range(1, n-1):
            mini = min(mini, max(arr[i], arr[i+1]))

        print(mini - 1)

if __name__ == "__main__":
    solve()