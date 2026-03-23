n, a, b = map(int, input().split())

for x in range((a + b) // n, 0, -1):
    if (a//x)>0 and (b//x)>0 and (a // x) + (b // x) >= n:
        print(x)
        break