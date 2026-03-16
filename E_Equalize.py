import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()

    unique_arr = [a[0]]
    for x in a[1:]:
        if x != unique_arr[-1]:
            unique_arr.append(x)

    l = 0
    sol = 1

    for r in range(len(unique_arr)):
        while unique_arr[r] - unique_arr[l] >= n:
            l += 1
        sol = max(sol, r - l + 1)

    print(sol)
