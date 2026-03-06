import heapq

def solve():
    n=int(input())
    s=list(map(int,input().split()))
    
    sol=0
    cards=[]

    for card in s:
        if card>0:
            heapq.heappush(cards,-card)
        else:
            if cards: sol+=-heapq.heappop(cards)
    
    print(sol)


t=int(input())
for _ in range(t):
    solve()