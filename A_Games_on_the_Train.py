def solve():
  n=int(input())
  a=list(map(int,input().split()))

  print((max(a)-min(a))+1)

t=int(input())

for _ in range(t):
  solve()