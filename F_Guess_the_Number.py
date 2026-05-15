import sys

n = int(input())

left = 1
right = n

while left < right:
    mid = (left + right + 1) // 2

    print(mid)
    sys.stdout.flush()

    response = input().strip()

    if response == "<":
        right = mid - 1
    else:
        left = mid

print("!", left)
sys.stdout.flush()