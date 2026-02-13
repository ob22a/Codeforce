import heapq

t = int(input())
while t :
    n, k = map(int, input().split()) # k bullets n monsters
    health = list(map(int,input().split()))
    distances = list(map(int,input().split()))

    heap = [] 
    for i in range(n):
        heap.append((abs(distances[i]), -health[i]))
    heapq.heapify(heap)
    steps = 0

    while heap:
        dist, h = heapq.heappop(heap)
        if dist-steps ==0:
            print("NO")
            heapq.heappush(heap,(dist,h))
            break
        
        cur_k = k
        steps+=1

        while cur_k!=0:
            # k will be either 0 or k+h
            # h will be 0 or k+h
            temp = cur_k
            cur_k = max(0,temp+h)
            h = min(0,temp+h)

            if cur_k>0 and h==0:
                if heap: dist,h = heapq.heappop(heap)
                else: break

        

        if h!=0:
            heapq.heappush(heap,(dist,h))
        

    if not heap: print("YES")
    t-=1