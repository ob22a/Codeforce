from functools import lru_cache

def solve():
    n,m=map(int,input().split())
    if n==m:
        print("YES")
        return 
    
    if n%3!=0 or m>2*n/3:
        print("NO")
        return 
    
    @lru_cache(None)
    def divide(num):
        if num<m:
            return False
        
        if num==m:
            return True
        
        if num%3==0: return divide(num//3) or divide(2*num//3)

        return False
    
    # dp= [False]*(n+1)
    # for i in range(1,n+1):
    #     if i>=m:
    #         if i==m:
    #             dp[i]=True
    #         else:
    #             dp[i]=False if i%3!=0 else dp[i//3] or dp[2*i//3]
    


    if divide(n):
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    solve()