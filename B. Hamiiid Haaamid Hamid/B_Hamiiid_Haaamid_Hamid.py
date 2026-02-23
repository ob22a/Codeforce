def solve():
    n,x = map(int,input().split())
    s=input()

    x-=1

    posl = -1
    posr = n

    for i in range(x,-1,-1):
        if s[i]=='#':
            posl=i
            break
    
    for i in range(x,n):
        if s[i]=='#':
            posr=i
            break

    # If left side is blocked 
    left1 = x+1
    right1 = n-posr+1

    # If right side is blocked
    left2 = posl+2
    right2=n-x

    print(max(min(left1,right1),min(left2,right2)))

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        solve()