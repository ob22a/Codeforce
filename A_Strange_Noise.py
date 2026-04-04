def solve():
    n = int(input())
    s=input()
    target = ["m","e","o","w"]
    idx = 0
    
    for c in target:
        if idx>=n or s[idx].lower()!=c:
            print("NO")
            return
        
        while idx<n and s[idx].lower()==c:
            idx+=1
    
    if idx!=n:
        print("NO")
        return
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()

    