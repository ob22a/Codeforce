import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n,s,x = map(int,input().split())
        a = list(map(int,input().split()))

        total = sum(a)
        if total > s or (total - s) % x != 0:
            print("NO")
            
        else: print("YES")

if __name__ == "__main__":
    solve()