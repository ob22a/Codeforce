t = int(input())
for _ in range(t):
    x = int(input())
    n = 3*x
    perm = [0]*n
    num=1

    for i in range(0,n,3):
        perm[i]=num
        num+=1
    
    for i in range(n):
        if perm[i]==0:
            perm[i]=num
            num+=1
    
    print(*perm)