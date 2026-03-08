def solve():
    n=int(input())
    s=input()

    sol=0
    count =0

    # If there is at least 3 consequetive empty cells then answer is 2 other wise it is count of empty ones

    i=0
    while i<n:
        j=i
        if s[i]=="#": 
            i+=1
            continue

        while j<n and s[i]==s[j]:
            count+=1
            j+=1
        
        if j-i>=3:
            print(2)
            return
        
        i=j
    
    print(count)

t = int(input())
for _ in range(t):
    solve()