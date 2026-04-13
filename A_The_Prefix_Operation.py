def solve():
    n,k=map(int,input().split())
    s=input()
    count_k = s.count('B')

    if count_k==k:
        print(0)
        return
    
    remaining = abs(k-count_k)
    if count_k<k:
        c_a = 0
        for i in range(n):
            if s[i]=='A':
                c_a+=1
            
            if c_a==remaining:
                print(1)
                print(i+1,'B')
                return
    
    c_b = 0
    for i in range(n):
        if s[i]=='B':
            c_b+=1
        
        if c_b==remaining:
            print(1)
            print(i+1,'A')
            return


t=int(input())
for _ in range(t):
    solve()