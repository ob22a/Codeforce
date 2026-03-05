def solve():
    s = input()    
    num_low_upper = [0]*3
    for c in s:
        if c.isdecimal():
            num_low_upper[0]+=1
        elif c.islower():
            num_low_upper[1]+=1
        else: num_low_upper[2]+=1
    
    if(all(x!=0 for x in num_low_upper)):
        print(s)
        return 
    
    a=list(s)
    n=len(a)
    hasZero = []

    for i in range(3):
        if num_low_upper[i]==0:
            hasZero.append(i)
    
    while not all(x!=0 for x in num_low_upper):
        largest = 0
        if num_low_upper[1]>num_low_upper[0]:
            if num_low_upper[2]>num_low_upper[1]:
                largest=2
            else:
                largest=1
        elif num_low_upper[2]>num_low_upper[0]:
            largest=2

        for i in range(n):
            if num_low_upper[largest]==1 or not hasZero:
                break

            match largest:
                case 0:
                    if(a[i].isdigit()):
                        if hasZero[-1]==1: 
                            a[i]='o'
                            num_low_upper[1]+=1
                        elif hasZero[-1]==2:
                            a[i]='O'
                            num_low_upper[2]+=1
                        hasZero.pop()
                        num_low_upper[largest]-=1
                case 1:
                    if(a[i].islower()):
                        if hasZero[-1]==0:
                            a[i]='1'
                            num_low_upper[0]+=1
                        elif hasZero[-1]==2:
                            a[i]='O'
                            num_low_upper[2]+=1
                        hasZero.pop()
                        num_low_upper[largest]-=1
                case 2:
                    if(a[i].isupper()):
                        if hasZero[-1]==0:
                            a[i]='1'
                            num_low_upper[0]+=1
                        elif hasZero[-1]==1:
                            a[i]='o'
                            num_low_upper[1]+=1
                        hasZero.pop()
                        num_low_upper[largest]-=1
    
    print("".join(a))
                

t = int(input())
for _ in range(t):
    solve()