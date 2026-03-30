def solve():
    n,k = map(int, input().split())
    s = input()

    last = -10e9 
    sol = 0

    for i in range(n):
        if s[i] == '1':
            if i - last >= k:
                sol += 1
                last = i
            else:
                last = i

    print(sol)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()