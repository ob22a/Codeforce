n = int(input())
a = list(int(input()) for _ in range(n))

def dfs(i,sol):
  if i==n:
    if sol%360==0:
      print('YES')
      exit(0)

    return
  
  dfs(i+1,sol+a[i])
  dfs(i+1,sol-a[i])

dfs(0,0)
print('NO')