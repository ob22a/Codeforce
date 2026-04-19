def solve():
    n,m = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(n)]

    visited = [[False for _ in range(m)] for _ in range(n)]
    vol = 0
    dir = [(1,0),(0,1),(-1,0),(0,-1)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] or grid[i][j]==0:
                continue
            
            cur_vol = 0
            stk = [(i,j)]
            visited[i][j]=True

            while stk:
                x,y = stk.pop()
                cur_vol+=grid[x][y]

                for dx,dy in dir:
                    nx = x+dx
                    ny = y+dy

                    if 0<=nx<n and 0<=ny<m and (not visited[nx][ny]) and grid[nx][ny]!=0:
                        stk.append((nx,ny))
                        visited[nx][ny]=True
            
            vol = max(vol,cur_vol)
    
    print(vol)


t = int(input())
for _ in range(t):
    solve()