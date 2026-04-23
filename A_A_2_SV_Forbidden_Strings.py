n = int(input())

chars = ['A', 'S', 'V']
seen = set()
ans = []

def f(state):
    if len(state) >= 3 and state[-3:] == ['S','V','A']:
        return

    if len(state) == n:
        seen.add(tuple(state))
        return

    for i in range(3):
        if not state or chars[i] != state[-1]:
            state.append(chars[i])
            f(state)
            state.pop()

f([])

print(len(seen))