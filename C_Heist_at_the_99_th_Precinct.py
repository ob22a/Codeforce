def solve():
    n = int(input())
    a = list(map(int,input().split()))


    if n%2!=0:
        print('YES')
        return
    
    a.sort()
    largest = a[-1]
    count = 0

    i = n-1
    while i>=0 and a[i]!=largest:
        count+=1
        i-=1
    
    if count%2!=0:
        print('YES')
        return

    if i>=0:
        count2=0
        while i>=0:
            val = a[i]
            while i>=0 and val==a[i]:
                count2+=1
                i-=1
        
            if count2%2!=0: 
                print("YES")
                return
        else: print("NO")
    else:
        print("NO")



t = int(input())

for _ in range(t):
    solve()