def solve():
    n = int(input())

    def is_fair(x):
        temp = x
        while temp:
            d = temp % 10
            if d != 0 and x % d != 0:
                return False
            temp //= 10
        return True

    while True:
        if is_fair(n):
            print(n)
            return
        n += 1
    

t = int(input())
for _ in range(t):
    solve()