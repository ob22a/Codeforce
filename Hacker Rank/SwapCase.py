def swap_case(s):
    sol=""
    for c in s:
        sol+=(c.lower()) if (c.isupper()) else c.upper()
    return sol

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
