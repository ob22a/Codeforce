def solve():
    n = int(input())
    s= input()

    if n == 1 and s!="1":
        print("No")
        return

    count_z = 0
    count_o = 0
    for i in range(n):
        if s[i]=="1":
            if count_o==0 and count_z>=2:
                print("No")
                return
            
            count_z=0
            count_o+=1
            
            if i<n-1 and s[i]==s[i+1]:
                print("No")
                return
        elif s[i]=="0":
            count_z+=1
            if count_z>2:
                print("No")
                return
    
    if count_z>=2:
        print("No")
        return

    print("Yes")

solve()