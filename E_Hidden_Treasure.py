n, m = map(int, input().split())

left = 1
right = n

for _ in range(m):
    clue = input().split()
    i = int(clue[-1])  
    
    if clue[2] == "left": 
        right = min(right, i - 1)
    else:  
        left = max(left, i + 1)

if left > right:
    print(-1)
else:
    print(right - left + 1)