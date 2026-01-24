'''
Docstring for B_Soldier_and_Bananas
tc= w(w+1)K/2 is the total cost of bananas
he needs to borrow n-tc
'''

k,n,w=map(int,input().split())
tc=(w*(w+1)//2)*k
if n>=tc:
    print(0)
else:
    print(tc-n)