def solve():
    n = int(input())
    a = n//3
    b = (n-a)//2
    c = n-(a+b)

    first_change = min(a-1,26-c)
    a-=first_change
    c+=first_change

    second_change = min(a-1,26-b)
    a-=second_change
    b+=second_change

    third_change = min(b-1,26-c)
    b-=third_change
    c+=third_change

    print("".join([chr(offset+ord('a')-1) for offset in [a,b,c]]))


t=int(input())
for _ in range(t):
    solve()