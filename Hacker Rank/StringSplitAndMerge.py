def split_and_join(line):
    sol=""
    for word in line.split():
        sol+=word+"-"
    return sol[:-1]

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
