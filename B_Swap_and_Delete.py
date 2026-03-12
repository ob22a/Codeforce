from collections import Counter
t = int(input())

def invert(s):
    return '0' if s=='1' else '1'

for _ in range(t):
    s=input()
    count = Counter(s)
    n=len(s)
    
    # Assume all are inverted and try to go as far as we can
    stop_idx = n
    for idx,c in enumerate(s):
        if count[invert(c)]==0:
            stop_idx=idx
            break
        count[invert(c)]-=1
    
    print(n-stop_idx)