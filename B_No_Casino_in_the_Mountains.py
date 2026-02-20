def solve():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))

        # Sliding window slide the window to find if weather can be good in all those days if not move the start as well
        l = 0
        r = 0
        hikes = 0

        while r<n:
            days = r-l+1
            if a[r]!=1 and days==k:
                l=r+2
                r=l
                hikes+=1
                continue
            
            if a[r]==1:
                l=r+1
                r=l
            else:
                r+=1
        
        print(hikes)

solve()