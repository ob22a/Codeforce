def solve():
  k=int(input())
  c=list(map(int,input().split()))

  if any(v>=3 for v in c):
    print("YES")
    return
  
  
  cnt=0
  for v in c:
    if v>=2:
      cnt+=1
    if cnt>=2:
      print("YES")
      return
  
  print("NO")


t=int(input())
for _ in range(t):
  solve()