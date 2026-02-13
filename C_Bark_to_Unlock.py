password = input()
num_of_words = int(input())

words = []
for _ in range(num_of_words):
    words.append(input())

# Bark one after the other but could be in different order and also not necessiarly distinct so he can repeat
# Since it is 2 word just find one that starts with password[1] and one that ends at password[0] or one that matches

canBreak = False

for word in words:
    if word == password:
        canBreak = True
        break

if canBreak:
    print("YES")
else :
    firstLetter = set([x for x in words if x[0]==password[1]])
    secondLetter = set([x for x in words if x[-1]==password[0]])

    if(len(firstLetter)!=0 and len(secondLetter)!=0):
        print("YES")
    else:
        print("NO")