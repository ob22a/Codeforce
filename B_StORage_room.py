def solve():
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    # print(a)

    val = -1
    for i in range(n):
        res = 0
        for j in range(n):
            res|=a[i][j]
        
        if val==-1:
            val=res
        elif val!=res:
            print("NO")
            return
    
    ans = [0]*n
    for i in range(n):
        res = a[i][i-1] if i==n-1 else a[i][i+1]
        for j in range(n):
            if i!=j: res&=a[i][j]
        ans[i]=res

    for i in range(n):
        for j in range(n):
            if i==j: continue
            if a[i][j]!=ans[i]|ans[j]:
                print("NO")
                return
    
    print("YES")
    print(*ans)

t = int(input())
for _ in range(t):
    solve()