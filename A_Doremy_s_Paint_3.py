from collections import Counter

def solve():
    n=int(input())
    a=list(map(int,input().split()))

    # for arr size 3 a b c we are saying a+b = b+c but this is only possible if a is equal to c so there can be at most 2 distinct numbers
    count = Counter(a)
    length = len(count)
    if length>2:
        print("NO")
        return 

    if length==1:
        print("YES")
        return

    f1,f2=count.values()

    if f1==f2 or (abs(f1-f2)==1 and n%2):
        print("YES")
    else:
        print("NO")


t=int(input())

for _ in range(t):
    solve()