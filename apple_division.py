n=int(input())
p=list(map(int,input().split()))

def gen(arr):
  sums=[]
  
  def dfs(i,sum):
    if i==len(arr):
      sums.append(sum)
      return
    
    dfs(i+1,sum)
    dfs(i+1,sum+arr[i])

  dfs(0,0)
  return sums

all_sums=gen(p)
sol = min(abs(2*s-sum(p)) for s in all_sums)

print(sol)