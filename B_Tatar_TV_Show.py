def solve():
  k,n=map(int,input().split())
  s=input()

  mapp = [0]*n

  for idx,chr in enumerate(s):
    if chr=="1":
      mapp[idx%n]+=1
  
  if(any(n%2!=0 for n in mapp)):
    print("NO")
    return 
  
  print("YES")

t=int(input())
for _ in range(t):
  solve()