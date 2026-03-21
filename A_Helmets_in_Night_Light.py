def solve():
    import sys
    input = sys.stdin.readline
    
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        hubs = sorted(zip(b, a))  # sort by relay cost
        # print(hubs)
        
        remaining = n
        total_cost = 0
        
        for cost, capacity in hubs:
            if cost >= p:
                break
            if remaining <= 1:
                break
            
            use = min(capacity, remaining - 1)
            total_cost += use * cost
            remaining -= use
        
        total_cost += remaining * p
        
        print(total_cost)


if __name__ == "__main__":
    solve()