t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))

    pos = []
    neg = []

    for n in l:
        if n>0:
            pos.append(n)
        else:
            neg.append(n)
    
    negate = 6 # We are always given 7 
    if neg: neg.sort()

    for i in range(len(neg)):
        if negate==0:
            break
        neg[i]*=-1
        negate-=1
    
    if pos: pos.sort()
    for i in range(len(pos)):
        if negate==0:
            break
        pos[i]*=-1
        negate-=1
    
    sol = sum(pos)+sum(neg)
    print(sol)