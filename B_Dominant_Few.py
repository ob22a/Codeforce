def solve():
    n=int(input())
    a=list(map(int,input().split()))

    a.sort()

    sum_crowd=a[0]+a[1]
    i=1

    sum_elite=a[-1]
    j=n-1

    while j>i:
        if sum_elite>sum_crowd:
            print("YES")
            return
        
        j-=1
        i+=1

        sum_elite+=a[j]
        sum_crowd+=a[i]

    print("NO")


t = int(input())
for _ in range(t):
    solve()