target = "ACTG"
n = int(input())
word = input()

count = 1e9
# It wraps around and target should be substring

def minDiff(str,subStr,count=0):
    for i in range(len(subStr)):
        diff = ord(str[i])-ord(subStr[i])
        count+= min(abs(diff),26-abs(diff))
    return count


for i in range(n-3):
    subStr = word[i:i+4]
    count = min(count,minDiff(target,subStr))

print(count)