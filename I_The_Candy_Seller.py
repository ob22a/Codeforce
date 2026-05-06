n,k=map(int,input().split())
a=list(map(int,input().split()))

i=0
sol=0
while k and i<n:
    sold = min(k,a[i])
    sol+=sold
    
    i+=1
    k-=sold

print(sol)