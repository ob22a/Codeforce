def solve():
    n=int(input())
    if n%3==0:
        print("Second")
        return
    
    print("First")

t = int(input())
for _ in range(t):
    solve()