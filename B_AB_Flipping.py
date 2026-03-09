def solve():
    n=int(input())
    s=list(input())

    a=0
    sol=0
    for i in range(n-1):
        if s[i]=="A" and s[i+1]=="B":
            sol+=a+1
            s[i+1]="A"
            a=0
        elif s[i]=="A":
            a+=1
        elif s[i]=="B":
            a=0
    
    print(sol)


t = int(input())
for _ in range(t):
    solve()