def solve():
    n = int(input())
    ravenCount = dict()

    for _ in range(n):
        m = int(input())
        for _ in range(m):
            raven,hour = input().split()
            if (raven,hour) not in ravenCount:
                ravenCount[(raven,hour)]=0
            else: ravenCount[raven,hour]+=1

        n = len(ravenCount)
        
    for count in ravenCount.values():
        if count/n>=0.8:
            print("YES")
            return
    print("NO")

solve()