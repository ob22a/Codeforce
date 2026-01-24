'''
Docstring for E_Only_Pluses
It seems like a greedy problem he can do the operation at most 5 times and in those he choose one integer and increment it by 1
What is the maximum value of a*b*c after at most 5 operations

Keep heap to track the smallest and the increment that 
'''
import heapq


n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    pq = [a, b, c]
    heapq.heapify(pq)
    for _ in range(5):
        x = heapq.heappop(pq)
        x += 1
        heapq.heappush(pq, x)
    result = pq[0] * pq[1] * pq[2]
    print(result)