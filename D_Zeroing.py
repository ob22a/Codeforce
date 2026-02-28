def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    prev = 0
    printed = 0
    
    for num in a:
        if printed == k:
            break
        
        if num - prev > 0:
            print(num - prev)
            prev = num
            printed += 1
    
    while printed < k:
        print(0)
        printed += 1

solve()