n,m = map(int,input().split())
answers = [input() for _ in range(n)]
marks = list(map(int,input().split()))

# optimistic means we would consider the answer with most frequency as the correct one and then use that to get the score

count = [[0]*5 for _ in range(m)]

def idx(c):
    if c=="A":
        return 0
    elif c=="B":
        return 1
    elif c=="C":
        return 2
    elif c=="D":
        return 3
    elif c=="E":
        return 4
    
    return -1 # Invalid

for student in answers:
    for i in range(m):
        j = idx(student[i])
        if j!=-1:
            count[i][j]+=1

ans = 0

for idx,qa in enumerate(count):
    max_ans = max(qa)
    ans+=max_ans*marks[idx]

print(ans)