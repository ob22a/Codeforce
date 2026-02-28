def solve():
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())

    smallest = min(a)
    largest = max(a)

    if smallest<=x<=largest: print("YES")
    else: print("NO")

T = int(input())
for _ in range(T):
    solve()