n,d=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
success = 0
i=n-1
j=0
while i>=j:
    largest = a[i]
    length_group = d//largest + 1 # Strictly greater 
    if i-j+1 <length_group:
        break

    j+=length_group-1
    i-=1
    success+=1

print(success)