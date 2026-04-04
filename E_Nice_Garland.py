n = int(input())
s = input()

# Brute force it 6 combinations of RGB check for each one

sol = float('inf')
correct = ""
combinations = ["GRB","GBR","RGB","RBG","BRG","BGR"]

for start in combinations:
    count = 0
    for i in range(n):
        if start[i%3]!=s[i]:
            count+=1
    if count<sol:
        sol = count
        correct=start

ans = list(s)
for i in range(n):
    ans[i]=correct[i%3]

print(sol)
print("".join(ans))