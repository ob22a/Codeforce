def solve():
    n,m,l,r = map(int,input().split())
    # we can just reduce l and keep r and if l becomes zero then reduce r
    while n!=m:
        if l<0: l+=1
        else: r-=1
        n-=1
    
    print(l,r)


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        solve()