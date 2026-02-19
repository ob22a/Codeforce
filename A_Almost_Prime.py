def computeAllPF(n):
    spf = [[0] for _ in range(n+1)]
    for i in range(2,n+1):
        if len(spf[i])==1: # Only 0
            for j in range(i,n+1,i):
                    spf[j].append(i)
    
    return spf

def solve():
    n = int(input())

    allPF = computeAllPF(n)
    #print(allPF)
    sol = 0

    for num in range(6,n+1): # 6 is the smallest almost prime
        val = num
        if len(allPF[num])==3:
             sol+=1
    
    print(sol)

solve()