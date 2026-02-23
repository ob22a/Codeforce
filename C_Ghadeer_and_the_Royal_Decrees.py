def maxAfterOp(a,operations):
    maximum = max(a)
    for op in operations:
        parsed = op.split()
        if int(parsed[1])<=maximum<=int(parsed[2]):
            if parsed[0]=='+': maximum+=1
            else: maximum-=1
        print(maximum,end=" ")
    print()
def solve():
    n,m=map(int,input().split())
    a = list(map(int,input().split()))
    op = [input() for _ in range(m)]
    maxAfterOp(a,op)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        solve()