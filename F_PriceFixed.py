import sys
input = sys.stdin.readline

n = int(input())

items = []
for _ in range(n):
    a, b = map(int, input().split())
    items.append([a, b])

items.sort(key=lambda x: x[1])

l = 0
r = n - 1

bought = 0
cost = 0

while l <= r:
    if bought >= items[l][1]:
        cost += items[l][0]
        bought += items[l][0]
        l += 1

    else:
        need = items[l][1] - bought
        take = min(need, items[r][0])

        cost += take * 2
        bought += take
        items[r][0] -= take

        if items[r][0] == 0:
            r -= 1

print(cost)
