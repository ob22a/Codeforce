def permutationExists(n,m,cards):
    for card in cards:
        if not all([(card[i]%n==card[i+1]%n) for i in range(m-1)]):
            print(-1)
            return False
        card.sort()

    permutation = [0]*n
    
    for row in range(n):
        permutation[cards[row][0]]=row+1

    for sol in permutation:
        print(sol,end=" ")
    print()

def solve():
    n,m = map(int,input().split())
    cards = [list(map(int,input().split())) for _ in range(n)]
    # print(cards)
    # each number in the set of card need to have a unique remainder when divided by n 
    # sort each row in the cards
    permutationExists(n,m,cards)
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()