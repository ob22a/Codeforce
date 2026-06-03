from bisect import bisect_left

n=int(input())
lucky = []

def lucky_numbers(x):
  if x>n:
    return 
  
  lucky.append(x)
  
  lucky_numbers(x*10+4)
  lucky_numbers(x*10+7)

lucky_numbers(0)
lucky.sort()

print(bisect_left(lucky,n))

"""
from bisect import bisect_left

n=int(input())
lucky = []
rank=0

def lucky_numbers(x):
  global rank
  if x>n:
    return 
  
  if x!=0:
    rank+=1
  
  lucky_numbers(x*10+4)
  lucky_numbers(x*10+7)

lucky_numbers(0)

print(rank)

"""