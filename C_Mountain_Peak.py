def solve():
    n = int(input())
    h = list(map(int, input().split()))
    
    for j in range(1, n-1): 
        if h[j-1] < h[j] > h[j+1]:
            print("YES")
            print(j, j+1, j+2)
            return
    
    print("NO")

t = int(input())
for _ in range(t):
    solve()