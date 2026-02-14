import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        unique = set()
        size = 0
        for i in range(n-1,-1,-1):
            if a[i] not in unique:
                unique.add(a[i])
                size += 1
            else:
                break
        print(n-size)

if __name__ == "__main__":
    solve()