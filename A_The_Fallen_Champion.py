w,t = map(int,input().split())
n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]

bestWin = 0
bestTime = float('inf')

for win,time in res:
    if win>bestWin:
        bestWin=win
        bestTime=time
    elif win==bestWin:
        bestTime=min(bestTime,time)

if w>bestWin or (w==bestWin and bestTime>=t):
    print("The Champion Saves the Accused")
else:
    print("The Fallen Champion")