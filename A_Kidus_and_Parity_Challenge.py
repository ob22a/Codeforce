def solve():
    n=int(input())
    a=list(map(int,input().split()))

    evens_count=0
    for num in a:
        if num%2==0:
            evens_count+=1
    
    odd_count=n-evens_count

    print(min(evens_count,odd_count))

t=int(input())

for _ in range(t):
    solve()