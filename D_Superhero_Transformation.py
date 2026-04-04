def solve():
    s = input()
    t = input()

    vowels = set(["a","e","i","o","u"])

    if len(s)!=len(t):
        print("NO")
        return 
    
    n = len(s)
    for i in range(n):
        if ((s[i] in vowels) ^ (t[i] in vowels)):
            print("NO")
            return
    
    print("YES")

solve()