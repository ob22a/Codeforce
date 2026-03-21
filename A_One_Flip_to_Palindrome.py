def solve():
    n = int(input())
    s = input()
    
    s = list(s)
    bad = []
    
    for i in range(n//2):
        if s[i] != s[n - 1 - i]:
            bad.append(i)
    
    if not bad:
        print("Yes")
        return
    
    l = bad[0]
    r = bad[-1]
    
    for i in range(l, r + 1):
        flipped = '1' if s[i] == '0' else '0'
        if flipped != s[n - 1 - i]:
            print("No")
            return
    
    print("Yes")


t = int(input())
for _ in range(t):
    solve()