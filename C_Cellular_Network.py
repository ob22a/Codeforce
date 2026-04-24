from bisect import bisect_right

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sol=0

for city in a:
    index = bisect_right(b,city)
    if index==0:
        min_distance = b[index]-city
    elif index==m:
        min_distance=city-b[index-1]
    else:
        min_distance=min(b[index]-city,city-b[index-1])
    
    sol=max(sol,min_distance)

print(sol)