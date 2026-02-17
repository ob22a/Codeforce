def computespf(n):
    spf = [0]*(n+1)
    for i in range(2,n+1):
        if spf[i]==0:
            for j in range(i,n+1,i):
                if spf[j]==0:
                    spf[j]=i
    
    return spf

def solve():
    n = int(input())
    # ways to get prime factors
        # get the smallest prime factor spf for each number and then use that to count the number of prime factors

    spf = computespf(n)
    sol = 0

    for num in range(6,n+1): # 6 is the smallest almost prime
        noDistinctPrimeFactors=0
        lastPrime = 0
        val = num

        while val>2:
            curPrime = spf[val]
            if lastPrime!=curPrime:
                lastPrime=curPrime
                noDistinctPrimeFactors+=1
            val//=curPrime
        
        if noDistinctPrimeFactors==2:
            sol+=1
    
    print(sol)

solve()