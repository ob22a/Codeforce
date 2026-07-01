from collections import defaultdict

n=int(input())
counter = defaultdict(list)

idx=2

for _ in range(n-1):
  p=int(input())
  counter[p].append(idx)
  idx+=1


for key,value in counter.items():
  count = 0
  for x in value:
    if x not in counter:
      count+=1

  if count<3:
    print("No")
    exit() 

print("Yes")