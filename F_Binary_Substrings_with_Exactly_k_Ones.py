k = int(input())
s = input()
n = len(s)

# At most method at most k and at most k+1

if k==0:
    count = 0
    sol = 0
    for c in s:
        if c=="1":
            count=0
        else:
            count+=1
            sol += count
    print(sol)

else:
    def helper(count):
        left = 0
        counter = [0,0]
        sol = 0
            
        for right in range(n):
            counter[int(s[right])]+=1

            while counter[1]>count:
                counter[int(s[left])]-=1
                left+=1
            
            sol+=right-left+1
        
        return sol

    print(helper(k)-helper(k-1))