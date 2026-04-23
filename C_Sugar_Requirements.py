from bisect import bisect_left
def solve():
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    x=[int(input()) for _ in range(q)]

    a.sort(reverse=True)
    prefix_sum= a[:]
    for i in range(1,n):
        prefix_sum[i]+=prefix_sum[i-1]

    for task in x:
        if prefix_sum[n-1]<task:
            print(-1)
        else:
            print(bisect_left(prefix_sum,task)+1)


t=int(input())
for _ in range(t):
    solve()