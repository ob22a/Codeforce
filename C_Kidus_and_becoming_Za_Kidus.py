def canFinish(d_h,mid):
    time=0
    for d,h in d_h:
        time+=(h+mid-1)//mid 
        if time>d:
            return False
    return True

def solve():
    n=int(input())
    h=list(map(int,input().split()))
    d=list(map(int,input().split()))

    max_ans = max(h)
    min_ans = min(((h[i]+d[i]-1)//d[i] for i in range(n)))

    d_h = [(d[i],h[i]) for i in range(n)]
    d_h.sort()

    while min_ans<max_ans:
        mid=(min_ans+max_ans)//2

        if canFinish(d_h,mid):
            max_ans=mid
        else:
            min_ans=mid+1
    
    print(min_ans)


t=int(input())
for _ in range(t):
    solve()