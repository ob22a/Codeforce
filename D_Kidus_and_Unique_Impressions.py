import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    l = [0]*n
    r = [0]*n
    
    maxv = 2*n + 5
    freq = [0]*maxv
    
    for i in range(n):
        l[i], r[i] = map(int, input().split())
        if l[i] == r[i]:
            freq[l[i]] += 1
    
    pref = [0]*maxv
    for i in range(1, maxv):
        pref[i] = pref[i-1] + (1 if freq[i] > 0 else 0)
    
    res = []
    
    for i in range(n):
        if l[i] == r[i]:
            if freq[l[i]] == 1:
                res.append('1')
            else:
                res.append('0')
        else:
            blocked = pref[r[i]] - pref[l[i]-1]
            length = r[i] - l[i] + 1
            
            if blocked < length:
                res.append('1')
            else:
                res.append('0')
    
    print("".join(res))