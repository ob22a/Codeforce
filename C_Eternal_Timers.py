def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = list(map(int,input().split()))

        isPossible = True
        for idx,num in enumerate(arr):
            moves = max((n-1-idx),idx)
            if num<=moves*2:
                isPossible=False
                break
        
        print("YES") if isPossible else print("NO")

if __name__ == "__main__":
    solve()