n=int(input())
a=list(map(int,input().split()))

a.sort()

days = 0
problems = 1

for num in a:
    if num>=problems:
        problems+=1
        days+=1

print(days)