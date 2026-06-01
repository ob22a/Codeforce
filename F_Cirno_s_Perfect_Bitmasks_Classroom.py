def solve():
  n=int(input())
  ans = 0
  and_idx = -1
  for i in range(32):
    if n & (1<<i):
      and_idx = i
      ans |= (1<<i)
      break
  
  if ans == n:
    for i in range(32):
      if i != and_idx:
        ans |= (1<<i)
        break

  print(ans)

t=int(input())
for _ in range(t):
  solve()