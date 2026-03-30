def solve():
    n,k = map(int, input().split())
    s = input()
    # No consequtive 1s of len k are allowed if that is the case we print("NO")
    ones_count = 0
    for idx in range(n):
        if s[idx]=="0":
            ones_count = 0
        else:
            ones_count+=1

        if ones_count >= k:
            print("NO")
            return 
    
    # Find permuation from 1-n where the zero's are large and the ones are small

    sol = [0]*n
    val = n

    for idx in range(n):
        if s[idx]=="0":
            sol[idx] = val
            val-=1
    
    for idx in range(n):
        if s[idx]=="1":
            sol[idx] = val
            val-=1
    
    print("YES")
    print(*sol)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()