from collections import defaultdict

def solve():
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    
    groups = defaultdict(list)
    for i in range(n):
        groups[u[i]].append(s[i])
    
    res = [0]*(n+1)

    for key in groups:
        arr = sorted(groups[key], reverse=True)
        
        # prefix sum
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        m = len(arr)
        
        # contribute to all k
        for k in range(1, m+1):
            teams = m // k
            if teams == 0:
                break
            res[k] += arr[teams*k - 1]
    
    print(*res[1:])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()