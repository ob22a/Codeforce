import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n,k = map(int, input().split())
        a = list(map(int, input().split()))
        isSorted = True
        for i in range(1, n):
            if a[i] < a[i-1]:
                isSorted = False
                break

        if (not isSorted) and k == 1:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    solve()