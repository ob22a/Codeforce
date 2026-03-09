def solve():
    n = int(input())
    a = list(map(int,input().split()))

    score1=0
    score2=0
    playerOneTurn=True

    i=0
    j=n-1

    while i<=j:
        if playerOneTurn:
            if a[i]>a[j]:
                score1+=a[i]
                i+=1
            else:
                score1+=a[j]
                j-=1
            playerOneTurn=not playerOneTurn
        else:
            if a[i]>a[j]:
                score2+=a[i]
                i+=1
            else:
                score2+=a[j]
                j-=1
            playerOneTurn=not playerOneTurn
    
    print(score1,score2)

solve()