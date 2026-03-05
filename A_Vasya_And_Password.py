def solve():
    s = list(input())
    
    digits = [i for i,c in enumerate(s) if c.isdigit()]
    lower  = [i for i,c in enumerate(s) if c.islower()]
    upper  = [i for i,c in enumerate(s) if c.isupper()]
    
    if digits and lower and upper:
        print("".join(s))
        return

    if not digits:
        if len(lower) > 1:
            s[lower.pop()] = '1'
        else:
            s[upper.pop()] = '1'

    if not lower:
        if len(digits) > 1:
            s[digits.pop()] = 'o'
        else:
            s[upper.pop()] = 'o'

    if not upper:
        if len(digits) > 1:
            s[digits.pop()] = 'O'
        else:
            s[lower.pop()] = 'O'

    print("".join(s))


t = int(input())
for _ in range(t):
    solve()