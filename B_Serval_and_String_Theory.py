def solve():
    n,k = map(int,input().split())
    s=input()
    
    if s < s[::-1] or (k>=1 and min(s)!=max(s)):
        print("YES")
        return
    
    print("NO")
     

t = int(input())
for _ in range(t):
    solve()