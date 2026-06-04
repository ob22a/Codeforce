a,b=map(int,input().split())

def factorial(n):
  if n==0:
    return 1
  return n*factorial(n-1)

print(factorial(min(a,b)))