t=int(input())

for _ in range(t):
    grid = [input() for _ in range(8)]

    for i in range(8):
        latin=[]
        for j in range(8):
            if grid[j][i].isalpha():
                latin.append(grid[j][i])
        if latin:
            print(''.join(latin))
    
    