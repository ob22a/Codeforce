n = int(input())
a = list(map(int, input().split()))
q = int(input())

last_time = [-1] * n
last_val = list(a)

max_2 = [0] * q 

for i in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1: 
        idx = query[1] - 1
        val = query[2]
        
        last_val[idx] = val
        last_time[idx] = i 
    else:
        max_2[i] = query[1]

for i in range(q - 2, -1, -1):
    max_2[i] = max(max_2[i], max_2[i+1])

for i in range(n):
    time = last_time[i]
    val = last_val[i]
    
    w = max_2[time+1] if time+1<q else 0
    
    a[i] = max(val, w)

print(*(a))