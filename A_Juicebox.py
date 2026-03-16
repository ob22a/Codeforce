# I hate this question

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    brand_cost = [0] * k 

    for _ in range(k):
        b, c = map(int, input().split())
        brand_cost[b - 1] += c  

    
    brand_cost.sort(reverse=True)
    
    ans = sum(brand_cost[:min(n, k)])
    print(ans)