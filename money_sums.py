n=int(input())
a=list(map(int,input().split()))

sums=set()

for num in a:
    new_sets = set()
    new_sets.add(num)
    
    for s in sums:
        new_sets.add(s+num)
    sums.update(new_sets)

print(len(sums))
print(*sorted(sums))