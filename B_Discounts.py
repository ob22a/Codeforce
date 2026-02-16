def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    a.sort()
    total_sum = sum(a)

    for discount in q:
        amount = total_sum - a[n-discount]
        print(amount)

if __name__ == "__main__":
    solve()