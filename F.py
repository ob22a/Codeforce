from collections import deque

def solve():
    n,m=map(int,input().split())
    s=input()

    ls = deque()
    east=True
    west=True

    for c in s:
        if c.isalpha() and len(ls)<m:
            if east:
                ls.append(c)
            elif west:
                ls.appendleft(c)
        elif c=='[':
            west=not west
        elif c==']':
            east=not east
        elif c=="<":
            if ls: ls.popleft()
        elif c==">":
            if ls: ls.pop()
    
    print("".join(ls))

t=int(input())

for _ in range(t):
    solve()