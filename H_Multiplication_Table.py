def solve():
    n=int(input())
    
    def radixConvert(num):
        res=[]
        while num:
            res.append(str(num%n))
            num//=n
        
        return "".join(res[::-1])
    
    for i in range(1,n):
        for j in range(1,n):
            print(radixConvert(i*j),end=" ")
        print()

solve()