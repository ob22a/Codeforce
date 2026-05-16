n=int(input())
d = n/100

#d=round(d,0)
last_d = d%10

#print(last_d,d)

if 0<=last_d<2.5:
    d-=last_d

elif 2.5<=last_d<=5:
    d+=5-last_d

elif 5<last_d<7.5:
    d-=last_d-5
else:
    d+=(10-last_d)

print(int(d*100))