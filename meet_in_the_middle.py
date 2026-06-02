from collections import Counter

n, x = map(int, input().split())
a = list(map(int, input().split()))

left = a[:n//2]
right = a[n//2:]

def gen(arr):
    sums = []

    def dfs(i, cur):
        if i == len(arr):
            sums.append(cur)
            return
        dfs(i + 1, cur)
        dfs(i + 1, cur + arr[i])

    dfs(0, 0)
    return sums

left_sums = gen(left)
right_sums = Counter(gen(right))

ans = 0
for s in left_sums:
    ans += right_sums[x - s]

print(ans)