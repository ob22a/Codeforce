def solve():
  n,x=map(int,input().split())
  graph=[0]*(n+1)
  
  for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u]+=1
    graph[v]+=1

  if graph[x]<=1 or n%2==0:
    print("Ayush")
  else:
    print("Ashish")
  

t=int(input())

for _ in range(t):
  solve()