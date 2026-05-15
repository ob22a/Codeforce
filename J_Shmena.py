from functools import cache


def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    # @cache
    # def f(idx,prev,x):
    #     if x < 0:
    #         return -float('inf')

    #     if idx == n:
    #         return 0
        
    #     not_take = f(idx+1,prev,x)
    #     take = 0

    #     if prev==-1 or a[idx]>a[prev]:
    #         take = 1+f(idx+1,idx,x)
    #     else:
    #         take = 1+f(idx+1,idx,x-1)
        
    #     return max(not_take,take)

    # print(f(0,-1,k))

    cur = [[0]*(k+1) for _ in range(n+1)]
    prev_dp = [[0]*(k+1) for _ in range(n+1)]

    for idx in range(n-1,-1,-1):
        for prev in range(-1,idx):
            for x in range(k+1):
                not_take = prev_dp[prev+1][x]
                take = 0

                if prev==-1 or a[idx]>a[prev]:
                    take = 1+prev_dp[idx+1][x]
                else:
                    take = 1+prev_dp[idx+1][x-1] if x>0 else 0
                
                cur[prev+1][x] = max(not_take,take)
            
            prev_dp=cur[:]
    
    print(cur[0][k])

t=int(input())
for _ in range(t):
    solve()