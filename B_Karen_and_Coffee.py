import sys
input = sys.stdin.readline

def solve():
    n,k,q=map(int,input().split())
    suggested = [list(map(int,input().split())) for _ in range(n)]
    questions= [list(map(int,input().split())) for _ in range(q)]
    
    MAX_SIZE = 200000
    suggestion_array = [0]*(MAX_SIZE+2)

    for left,right in suggested:
        suggestion_array[left]+=1
        suggestion_array[right+1]-=1
    
    # Build the full thing
    for i in range(1,MAX_SIZE+1):
        suggestion_array[i]+=suggestion_array[i-1]
    
    # In validate those less than k
    for i in range(MAX_SIZE+1):
        suggestion_array[i] = 1 if suggestion_array[i] >= k else 0
    
    # Prefix sum this again so that count would be represented
    for i in range(1,MAX_SIZE+1):
        suggestion_array[i]+=suggestion_array[i-1]
    
    for left,right in questions:
        print(suggestion_array[right]-suggestion_array[left-1])

solve()