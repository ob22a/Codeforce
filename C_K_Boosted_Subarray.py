def maxSubarraySum(a):
    current=max_sum=a[0]

    for i in range(1,len(a)):
        current=max(current+a[i],a[i])
        max_sum=max(max_sum,current)
    
    return max_sum

def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    max_subarray_sum=maxSubarraySum(a)

    print(max(k*max_subarray_sum,max_subarray_sum//k))

t=int(input())
for _ in range(t):
    solve()