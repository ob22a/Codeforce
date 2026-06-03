n=int(input())
HOUSE_COST = 1234567
CARS_COST = 123456
COMPUTERS_COST = 1234

for a in range(n//HOUSE_COST,-1,-1):
    rem = n - HOUSE_COST*a

    for b in range(rem//CARS_COST,-1,-1):
        left = rem - CARS_COST*b

        if left>=0 and left%COMPUTERS_COST==0:
            print("YES")
            exit(0)

print("NO")
