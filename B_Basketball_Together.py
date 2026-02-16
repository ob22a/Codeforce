def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    
    return r

def solve():
    n,d = map(int,input().split())
    p = list(map(int,input().split()))
    # Match the largest and smallest elements if that doesn't win us matches then add more smaller players until we have enough to win
    p.sort()

    start_idx = 0
    end_idx = 0

    max_idx = binary_search(p, d)
    wins = n-max_idx-1

    while end_idx <= max_idx:
        players = end_idx - start_idx + 1 
        if max_idx != end_idx:
            players += 1
        score = p[max_idx] * players
        if score > d:
            wins += 1
            end_idx+=1
            start_idx=end_idx
            max_idx-=1
        else:
            end_idx+=1

    print(wins)

if __name__ == "__main__":
    solve()