def solve():
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    
    TARGET = 2023
    product = 1
    for num in b:
        product*=num

    if TARGET%product!=0:
        print("NO")
        return

    removed = TARGET//product
    removed_arr = [removed]

    for _ in range(k-1):
        removed_arr.append(1)
    
    print("YES")
    print(*removed_arr)

t = int(input())
for _ in range(t):
    solve()