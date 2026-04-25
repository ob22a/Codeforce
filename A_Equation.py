import math

n=int(input())

def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


i = n + 4

while True:
    if not is_prime(i) and not is_prime(i - n):
        print(i, i - n)
        break
    i += 1

# LIMIT = 10**9+1
# arr = [True]*LIMIT

# for i in range(2,LIMIT):
#     if arr[i]==False:
#         if i-n>=0 and arr[i-n]==False:
#             print(i,i-n)
#             break
#     for j in range(i+i,LIMIT,i):
#         arr[j]=False