def solve():
  n=int(input())
  a=list(map(int,input().split()))

  b=sorted(a)
  sol = 1<<18 # 2*18 is a good upper bound 
  sol-=1

  for i in range(n):
    if a[i]!=b[i]:
      sol&=a[i]
  
  print(sol)

t=int(input())
for _ in range(t):
  solve()