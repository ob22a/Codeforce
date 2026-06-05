def solve():
  n=int(input())
  s=input()

  def dvc(string,target):
    if len(string)==1:
      #print(int(string!=target),string,target)
      return int(string!=target)
    
    length = len(string)
    
    left=0
    right=0

    for i in range(length//2):
      if string[i]!=target:
        left+=1
    
    for i in range(length//2,length):
      if string[i]!=target:
        right+=1

    #print("DEBUG:",left,right,length,string)

    left += dvc(string[length//2:length],chr(ord(target)+1))
    right += dvc(string[:length//2],chr(ord(target)+1))
    
    return min(left,right)
  
  print(dvc(s,'a'))


t=int(input())
for _ in range(t):
  solve()