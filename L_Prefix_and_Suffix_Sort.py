def canBeSorted(a,mid):
    temp = a[:]
    if mid>0:
        temp[:mid]=sorted(temp[:mid])
        temp[-mid:]=sorted(temp[-mid:])
    
    return temp==sorted(a)

def solve():
    n=int(input())
    a=list(map(int,input().split()))

    left=0
    right=n

    while left<right:
        mid=(left+right)//2
        if canBeSorted(a,mid):
            right=mid
        else:
            left=mid+1
    
    print(left)


t=int(input())

for _ in range(t):
    solve()