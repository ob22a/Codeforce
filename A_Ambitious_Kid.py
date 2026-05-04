n=int(input())
a=list(map(int,input().split()))

hasZero = any(x == 0 for x in a)

if hasZero:
    print(0)
    exit()

largest_neg = max([x for x in a if x < 0], default=float('-inf'))
smallest_pos = min([x for x in a if x > 0], default=float('inf'))

print(min(abs(largest_neg), abs(smallest_pos)))