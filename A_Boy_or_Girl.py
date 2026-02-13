# if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female

username = input()
seen = set(username)

if(len(seen)%2==0): print("CHAT WITH HER!")
else: print("IGNORE HIM!")