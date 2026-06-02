n=int(input())
sol=0

def rec(base):
  global sol
  
  if base<=n: sol+=1
  if base>n: return
  rec(base*10)
  rec(base*10+1)

rec(1)
print(sol)