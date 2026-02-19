def solve():
    t = int(input())
    for _ in range(t):
        x = int(input())
        smallestDigit = 9
        while x:
            smallestDigit=min(smallestDigit,x%10)
            x//=10
        print(smallestDigit)

solve()