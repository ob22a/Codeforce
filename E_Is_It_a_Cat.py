def solve():
    n=int(input())
    s=input()

    cat_sound="meow"
    cat_idx=0

    i=0
    while i<n and cat_idx<4:
        if s[i].lower()!=cat_sound[cat_idx]:
            print("NO")
            return
        
        while i<n and s[i].lower()==cat_sound[cat_idx]:
            i+=1
        cat_idx+=1
    

    print("YES" if cat_idx==4 and i==n else "NO")

t=int(input())
for _ in range(t):
    solve()