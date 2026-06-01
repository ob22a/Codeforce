def solve():
  s=input()
  count = 0
  
  i= 0
  while i <= len(s) - 1:
    if s[i] == "0":
      j = i
      while j < len(s) and s[j] == "0":
        j += 1
      count+=1
      i = j
    else:
      i += 1

  print(min(count,2))

t=int(input())
for _ in range(t):
  solve()