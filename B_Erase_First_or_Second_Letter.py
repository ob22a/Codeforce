def solve():
  n=int(input())
  s=input()

  seen = set()
  ans = 0

  for ch in s:
      seen.add(ch)
      ans += len(seen)

  print(ans)


t = int(input())
for _ in range(t):
  solve()