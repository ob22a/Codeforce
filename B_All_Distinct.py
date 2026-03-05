from collections import Counter
import math

def solve():
    n=int(input())
    a=list(map(int,input().split()))

    count = Counter(a)
    sol = 0
    no_unique = len(count)
    even_freq = 0

    if n==no_unique:
        print(n)
        return 
    
    for val in count.values():
        if val%2!=0:
            no_unique-=1
            sol+=1
        else:
            even_freq+=1

    if even_freq%2==0:
        sol+=even_freq
    else:
        sol+=even_freq-1

    print(sol)

t=int(input())
for _ in range(t):
    solve()