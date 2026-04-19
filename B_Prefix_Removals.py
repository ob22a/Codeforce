def solve():
    s = input()
    count = [0]*26
    def charIdx(c):
        return ord(c)-ord('a')

    for c in s[::-1]:
        count[charIdx(c)]+=1

    for i in range(len(s)):
        idx = charIdx(s[i])
        if count[idx]!=1:
            count[idx]-=1
        else:
            break
    
    startPoint = i

    print(s[startPoint:])

t=int(input())
for _ in range(t):
    solve()