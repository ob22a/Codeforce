from math import log2

def solve():
    n=int(input())
    length = int(log2(n))

    print((1<<length)-1)


t=int(input())
for _ in range(t):
    solve()