import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        max_num = arr[0]
        min_num = arr[0]
        for num in arr:
            max_num = num | max_num
            min_num = num & min_num

        print(max_num - min_num)

if __name__ == "__main__":
    solve()