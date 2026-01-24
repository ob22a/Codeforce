'''
Docstring for D_Even_Odds

for n initially arrange the odds then the evens
and find what number is at the kth position

TLE will happen if we iterate through 1 to n and count odds and evens
so let's make a math formula 

if k is less than or equal to (n+1)//2 then it's an odd number other wise even
if it is odd the formula for finding it is (k*2-1)
if it is even the formula for finding it is (k-(n+1)//2)*2
'''
n,k = map(int,input().split())

if k <= (n+1)//2:
    print((k*2-1))
else:
    print((k-(n+1)//2)*2)