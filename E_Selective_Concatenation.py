import sys
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n==k:
        counter = 1
        for idx in range(1,n,2):
            if a[idx]!=counter:
                print(counter)
                return
            counter+=1
        
        print(counter)
        return
    
    for i in range(1,n-k+2):
        if a[i]!=1:
            print(1)
            return
    
    print(2)

t = int(input())
for _ in range(t):
    solve()