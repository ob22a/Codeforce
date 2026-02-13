n = int(input())
word = input()

letters = set(word.lower())

if(len(letters)!=26): print("NO")
else: print("YES")