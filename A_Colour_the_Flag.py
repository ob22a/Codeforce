def solve():
    t = int(input())
    for _ in range(t):
        n,m= map(int,input().split())
        grid = [list(input()) for _ in range(n)]
        
        # better approach to solve this is using the chessboard pattern this is what the question is asking so first find a colored index and fill based on that from there and if a rule is violated then print NO

        isFound = False
        redEven = True
        isPossible = True

        for i in range(n):
            for j in range(m):
                new_idx = i+j
                idx_even = (new_idx%2 == 0)
                if (not isFound) and (grid[i][j] == 'R' or grid[i][j] == 'W'):
                    isFound = True
                    redEven = (new_idx%2 == 0) if grid[i][j] == 'R' else (new_idx%2 != 0)
                elif isFound:
                    if grid[i][j] != '.' :
                        isRed = grid[i][j] == 'R'

                        valid = redEven == (idx_even == isRed)
                        if not valid:
                            isPossible = False
                            break
                    else:
                        val = 'R' if (redEven == idx_even) else 'W'
                        grid[i][j] = val
        if not isPossible:
            print("NO")
        else:
            print("YES")
            for i in range(n):
                for j in range(m):
                    if grid[i][j] !='.':
                        print(grid[i][j],end="")
                    else:
                        val = 'R' if (redEven == ((i+j)%2 == 0)) else 'W'
                        print(val,end="")
                print()



if __name__ == "__main__":
    solve()