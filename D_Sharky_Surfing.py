import heapq
import sys
input = sys.stdin.readline

def solve():
        n, m, L = map(int, input().split())

        hurdles = [tuple(map(int, input().split())) for _ in range(n)]
        powerups = [tuple(map(int, input().split())) for _ in range(m)]

        heap = []
        k = 1
        count = 0
        j = 0  

        for l, r in hurdles:
            while j < m and powerups[j][0] < l:
                heapq.heappush(heap, -powerups[j][1])
                j += 1
                
            needed = r - l + 2

            while k < needed:
                if not heap:
                    print(-1)
                    return
                k += -heapq.heappop(heap)
                count += 1
       
        print(count)

t = int(input())
for _ in range(t):
    solve()