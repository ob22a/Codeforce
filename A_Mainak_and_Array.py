def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a= list(map(int,input().split()))

        sol = max(max(a)-a[0],a[-1]-min(a))

        for i in range(1,n):
            sol = max(sol,a[i-1]-a[i])

        print(sol)

if __name__ == "__main__":
    solve()