from collections import Counter

def solve():
    n,k=map(int,input().split())
    s=input()

    count = Counter(s)
    oddCount = 0

    for c in count.values():
        if c%2==1 and oddCount>0 and k==0:
            print("NO")
            return
        elif c%2==1 and k==0:
            oddCount+=1
        elif c%2==1 and k>0:
            k-=1
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()