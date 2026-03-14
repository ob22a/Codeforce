def solve():
    k = int(input())
    a = list(map(int,input().split()))

    total = sum(a)
    if total<k:
        print(-1)
        return
    
    a.sort()
    sol = 0
    total = 0
    if k>0: 
        for i in range(11,-1,-1):
            total+=a[i]
            sol+=1
            if total>=k:
                break
    
    print(sol)

solve()