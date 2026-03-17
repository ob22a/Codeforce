import sys

input = sys.stdin.readline

def solve():
    n,k=map(int,input().split())
    a = list(map(int,input().split()))

    sol = float('inf') 
    prod = 1

    for num in a:
        prod*=num
    
    if prod%k==0:
        print(0)
        return

    if k==2:
        print(1)
        return
    
    for num in a:
        sol = min(sol,(k - num % k) % k)
    
    if k==4:
        evens = 0
        for num in a:
            if num%2==0:
                evens+=1
        
        sol = min(sol,2-evens)
    
    print(sol)

t = int(input())
for _ in range(t):
    solve()


"""
Initial wrong approach
It is wrong because each number is not independent we can increase one one two numbers and reach the answer

    for num in a:
        quotient = num//k
        larger_muliple = k*(quotient+1)
        prod//=num

        for number in range(num+1,larger_muliple+1):
            if (prod*number)%k==0:
                ans = min(ans,number-num)
        
        prod*=num
        
    
    print(ans)
"""