from collections import Counter
def solve():
    n = int(input())
    s = input()

    no_l = 0

    for c in s:
        if c=="L":
            no_l+=1
    
    no_o = n-no_l

    left_l = 0 
    left_o = 0

    for c in s:
        if c=="L":
            left_l+=1
            no_l-=1
        else:
            left_o+=1
            no_o-=1
        
        if left_l!=no_l and left_o!=no_o  and not (no_l==0 and no_o==0):
            print(left_l+left_o)
            return
    
    print(-1)

solve()