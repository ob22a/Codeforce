def solve():
    n=int(input())
    k=list(map(int,input().split()))

    seen = set()
    sol = 0
    left = 0

    for right in range(n):
        while k[right] in seen:
            seen.remove(k[left])
            left+=1
        
        seen.add(k[right])
        sol = max(sol,right-left+1)

    print(sol)

solve()