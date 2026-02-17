def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total = sum(arr)
        if total % n != 0:
            print(-1)
        else:
            arr.sort()
            target = total//n
            increment = 0 
            for num in arr:
                if num<target:
                    increment+=abs(target-num)

            amount =0
            count = 0
            for i in range(n-1,-1,-1):
                if amount<increment: count+=1
                amount+=abs(arr[i]-target)
                if amount>=increment:
                    break
            print(count)
   
if __name__ == '__main__':
    solve()