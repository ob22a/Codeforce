def solve():
  n=int(input())
  a=list(map(int,input().split()))

  p1=[0]*(n+1)
  p3=[0]*(n+1)

  for i in range(1,n+1):
    if a[i-1]==1:
      p1[i]+=1
    elif a[i-1]==3:
      p3[i]+=1
    
    p1[i]+=p1[i-1]
    p3[i]+=p3[i-1]

  # Compute k-2p3[k] because f(i)<=f(j)
  f = [k-(2*p3[k+1]) for k in range(n)]

  # Compute suffix max

  suffix=[-float('inf')]*n
  suffix[n-2]=f[n-2]

  for i in range(n-3,-1,-1):
    suffix[i]=max(f[i],suffix[i+1])

  for i in range(n-2):
    if 2*p1[i+1]>=i+1:
      if suffix[i+1]>=f[i]:
        print("YES")
        return

  print("NO")
    

t=int(input())
for _ in range(t):
  solve()