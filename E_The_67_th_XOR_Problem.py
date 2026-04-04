t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    sol = 0
    # print(a)

    for i in range(n):
        for j in range(i+1,n):
            sol = max(sol,a[i]^a[j])
    
    print(sol)