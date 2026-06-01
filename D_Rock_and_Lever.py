t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))

  # Ask Danik for the answer
  # Let's use a 32 bit dictionary to count the number of 1s in each bit position

  count=0
  d = [0]*32
  
  for i in range(n):
    for j in range(31,-1,-1):
      if a[i] & (1<<j):
        if d[j]>0:
          count+=d[j]
        d[j]+=1
        break
    
  print(count)