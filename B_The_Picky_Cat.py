t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    x = abs(a[0])
    
    small = 0  
    big = 0   
    
    for i in range(1, n):
        if abs(a[i]) < x:
            small += 1
        else:
            big += 1
    
    k = (n + 1) // 2 
    need = k - 1  
    
    ok = False

    if small <= need or big<=need:
        ok = True
    
    print("YES" if ok else "NO")