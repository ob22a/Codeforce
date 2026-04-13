from collections import deque

n,m=map(int,input().split())
a = deque(map(int,input().split()))

buses = 0

while a:
    front = a.popleft()
    buses+=1

    empty = m-front

    while a and empty>=a[0]:
        empty-=a.popleft()
    
print(buses)