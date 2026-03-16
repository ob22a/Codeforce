import math

def countNumberOfDivsions(a,b):
    count = 0
    while a:
        a//=b
        count+=1
    
    return count

def solve():
    a,b=map(int,input().split())
    sol = 0
    if b==1:
        sol+=1
        b+=1
    
    cur_sol = sol

    sol+=countNumberOfDivsions(a,b)
    check_upto = sol

    for _ in range(check_upto):
        b+=1
        cur_sol+=1
        sol=min(sol,cur_sol+countNumberOfDivsions(a,b))
    
    print(sol)

t = int(input())
for _ in range(t):
    solve()