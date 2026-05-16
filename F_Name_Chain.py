from collections import defaultdict
from collections import deque

def solve():
    n=int(input())
    names = list(input().split() for i in range(n))
    
    graph = defaultdict(list)

    for fn,ln in names:
        graph[fn].append(ln)
        graph[ln].append(fn)
    

    def bfs(start):
        queue = deque([start])
        seen=set([start])

        dist = {start:0}
        parent = {start:None}
        farthest = start

        while queue:
            name = queue.popleft()

            if dist[name]>dist[farthest]:
                farthest=name

            for n in graph[name]:
                if n not in seen:
                    dist[n]=dist[name]+1
                    parent[n]=name
                    seen.add(n)

                    queue.append(n)
        
        return parent,farthest
    

    def reconstruct(end,parent):
        cur = end
        path = []

        while cur:
            path.append(cur)
            cur=parent[cur]
        
        return path
    
    start_point = list(graph.keys())[0]

    _,a = bfs(start_point)
    p,b=bfs(a)

    path = reconstruct(b,p)

    print(len(path))
    print(" ".join(path))


t=int(input())

for _ in range(t):
    solve()