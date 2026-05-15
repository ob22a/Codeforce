t=int(input())

for _ in range(t):
    s=list(input())
    sol=[]
    
    # moving left
    temp = s[:]
    temp[0]=chr(ord(temp[0])-1)

    while temp[0]>='a':
        sol.append("".join(temp))
        temp[0]=chr(ord(temp[0])-1)
    
    # moving right
    temp = s[:]
    temp[0]=chr(ord(temp[0])+1)

    while temp[0]<='h':
        sol.append("".join(temp))
        temp[0]=chr(ord(temp[0])+1)
    
    # moving up
    temp = s[:]
    temp[1]=chr(ord(temp[1])+1)

    while temp[1]<='8':
        sol.append("".join(temp))
        temp[1]=chr(ord(temp[1])+1)
    
    # moving down
    temp = s[:]
    temp[1]=chr(ord(temp[1])-1)

    while temp[1]>='1':
        sol.append("".join(temp))
        temp[1]=chr(ord(temp[1])-1)
    
    print("\n".join(sol))