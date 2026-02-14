import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        # Ans is always 0 1 or 2 if all are zero is it zero
        # if there is uninterupted sequence of non zero numbers or if zeros are all consecutive to one another it is 1
        # else it is 2 because we can mex the whole thing and mex that 

        if all(x == 0 for x in arr):
            print(0)
            continue

        # Check if there is an uninterrupted sequence of non-zero numbers
        non_zero_sequence = False
        idx = 0
        for i in range(n):
            if arr[i] != 0:
                non_zero_sequence = True
            elif non_zero_sequence:
                break
            idx+=1
        
        if idx == n:
            print(1)
            continue

        interrupted = False
        for i in range(idx, n):
            if arr[i] != 0:
                interrupted = True
                break

        if interrupted:
            print(2)
        else:
            print(1)

if __name__ == "__main__":
    solve()