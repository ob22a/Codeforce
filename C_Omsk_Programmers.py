def solve():
  a,b,x=map(int,input().split())
  cnt = 0
  ans = max(a,b)-min(a,b)

  while a!=b:
    if ans<=cnt:
      break

    if a>b:
      a//=x
    else:
      b//=x
    
    cnt+=1

    ans = min(ans,max(a,b)-min(a,b)+cnt)
  

  print(ans)
  
t=int(input())
for _ in range(t):
  solve()