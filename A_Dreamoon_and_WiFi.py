drazil=input()
dreamoon=input()

target=0
for c in drazil:
  if c=="+":
    target+=1
  else:
    target-=1

c_tl = [0,0] # Correct ones and total leaf nodes

def dfs(i,s):
  if i==len(dreamoon):
    if s==target:
      c_tl[0]+=1
    c_tl[1]+=1
    return
  
  if dreamoon[i]=="+":
    dfs(i+1,s+1)
  elif dreamoon[i]=="-":
    dfs(i+1,s-1)
  else:
    dfs(i+1,s+1)
    dfs(i+1,s-1)

dfs(0,0)

print(c_tl[0]/c_tl[1])