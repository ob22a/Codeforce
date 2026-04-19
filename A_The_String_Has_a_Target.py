def solve():
    n = int(input())
    s= input()

    sol = list(s)

    i = 0

    for idx in range(1,n):
        if s[idx]<=s[i]:
            i=idx

    print(s[i],end="")

    for idx in range(n):
        if idx!=i:
            print(s[idx],end="")
    
    print()
    
t = int(input())

for _ in range(t):
    solve()