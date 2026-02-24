def missingNumber(a):
    # ignore zeros
    # find the missing number from consequetive list

    # place num at idx num-1
    b= a[:]
    n = len(b)

    for i in range(n):
        if b[i]==0: continue
        while b[i]!=0 and b[i] != b[b[i]-1]:
            # initially it was b[i],b[b[i]-1]=b[b[i]-1],b[i] but when the values swap the value of b[i] changes and the indexing will get disrupted as well
            val1 = b[i]
            val2 = b[b[i]-1]
            b[i] = val2
            b[val1-1]=val1
    
    for i in range(n):
        if b[i]==0:
            return i+1

def solve():
    n = int(input())
    grid = [list(map(int,input().split())) for _ in range(n)]
    sol =[0]*2*n

    for i in range(n):
        for j in range(n):
            sol[i+j+1]=grid[i][j]
    
    sol[0]=missingNumber(sol)
    print(*sol)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        solve()