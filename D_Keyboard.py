t = int(input())
for _ in range(t):
    s = input()
    n = len(s)

    sol = set()
    
    i = 0
    while i<n:
        if i<n-1 and s[i]==s[i+1]:
            i+=2
            continue
        sol.add(s[i])
        i+=1
    
    print("".join(sorted(sol)))