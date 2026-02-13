n = int(input())
cards = list(map(int,input().split()))

# Sereja Dima Score

left = 0 
right = n-1

sereja_turn = True
sereja_score = 0
dima_score = 0 

while(left<=right):
    if(sereja_turn):
        if(cards[left]>cards[right]):
            sereja_score+=cards[left]
            left+=1
        else:
            sereja_score+=cards[right]
            right-=1
        sereja_turn = not sereja_turn
    else:
        if(cards[left]>cards[right]):
            dima_score+=cards[left]
            left+=1
        else:
            dima_score+=cards[right]
            right-=1
        sereja_turn = not sereja_turn

print(sereja_score, dima_score)