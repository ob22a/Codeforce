n = int(input())
phonebook = {}
for _ in range(n):
    name, num = input().split()
    phonebook[name] = num

while True:
    try:
        name = input()
    except EOFError:
        break  

    if name in phonebook:
        print(name + "=" + phonebook[name])
    else:
        print("Not found")
