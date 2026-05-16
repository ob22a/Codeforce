def solve():
    n,m=map(int,input().split())
    price_amount = list(list(map(int,input().split())) for _ in range(n))

    total = 0

    for _ in range(m):
        num=int(input())

        p,cur_am = price_amount[num-1]

        if cur_am>0:
            total+=p
        
        price_amount[num-1][1]-=1
    
    print(total)

t=int(input())

for _ in range(t):
    solve()