n = int(input())
s = list(map(int,input().split()))

startRest = 0
i=0
while i<n and s[i]==1:
    i+=1
    startRest+=1

endRest = 0
j = n-1

while j>=0 and s[j]==1:
    j-=1
    endRest+=1

sol = startRest + endRest

count = 0

for right in range(i,j+1):
    if s[right]==0:
        sol = max(sol,count)
        count=0
    else:
        count+=1

print(sol)