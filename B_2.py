from bisect import bisect_left

l,r=map(int,input().split())
lucky=[]

def lucky_number(x):
    if x>r*10: # Safe upper bound to avoid unnecessary calculations
        return
    if x!=0:
        lucky.append(x)
    lucky_number(x*10+4)
    lucky_number(x*10+7)

lucky_number(0)
lucky.sort()

sol=0 

#print(lucky)

while l<=r:
    idx = bisect_left(lucky,l)
    #print(f"Current l: {l}, idx: {idx}, lucky[idx]: {lucky[idx] if idx < len(lucky) else 'N/A'}")
    if idx >= len(lucky):
        idx-=1

    length = min(r, lucky[idx]) - l + 1
    sol+=(length)*lucky[idx]
    l=lucky[idx]+1

print(sol)