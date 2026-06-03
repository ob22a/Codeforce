n=int(input())

fibo = [1, 1]

while fibo[-1] + fibo[-2] <= n:
    fibo.append(fibo[-1] + fibo[-2])

fibo_set = set(fibo)

sol = []

for i in range(1,n+1):
  sol.append("O" if i in fibo else "o")

print("".join(sol))