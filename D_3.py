n=int(input())

def is_lucky(num):
  if num==0:
    return False
  
  while num:
    last_digit = num%10
    if last_digit!=4 and last_digit!=7:
      return False
    num//=10
  
  return True

count=0
while n:
  last = n%10
  if last==4 or last==7:
    count+=1
  n//=10

#print(count)

print("YES") if is_lucky(count) else print("NO")