n = int(input())
a = [0] * (2**(n+1))

vals = list(map(int, input().split()))
for i in range(2, 2**(n+1)):
    a[i] = vals[i-2]

ans = 0

def dfs(i):
    global ans
    if i * 2 >= len(a):
        return 0
    
    left = dfs(i * 2) + a[i * 2]
    right = dfs(i * 2 + 1) + a[i * 2 + 1]
    
    ans += abs(left - right)
    
    return max(left, right)

dfs(1)
print(ans)