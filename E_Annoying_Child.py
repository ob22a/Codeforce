# fast IO
import sys
input = sys.stdin.readline
print = sys.stdout.write


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort(reverse=True)

        even = []
        maxOdd = 0 # since we need only the max odd

        for num in a:
            if num % 2:
                maxOdd = max(maxOdd, num)
            else: 
                even.append(num)

        sumEven = sum(even) # we can use a prefix sum instead

        # the last even (min even) is used in case 3 and the first odd (max odd) is used in case 2
        lastEvenFirstOdd = even[-1] if even else maxOdd

        # case 1
        if not maxOdd:
            print(" ".join(["0"]*n) + "\n")
            continue
        
        # k = 1 for case 2, 3
        print(str(maxOdd) + " ")
        lastNum = maxOdd # to add even numbers to it for the first part of case 3

        # pointer for even numbers to handle first part of case 3
        e = 0
        m = len(even)
        for i in range(1, n):
            if i > m : # second part of case 3 / case 2
                remaining = i- m

                if remaining % 2: # handling the two sub cases for case 2, 3

                    print("0 ") if i == n-1 else print(str(sumEven+maxOdd-lastEvenFirstOdd) + " ") #smallest even so that it can empty initially
                    # when there are no even numbers it alternate between the max and 0 0+maxOdd-maxOdd
                else:
                    print(str(sumEven+maxOdd) + " ")

            else: # first part of case 3
                lastNum += even[e]
                print(str(lastNum) + " ")
                e += 1

        print("\n")


if __name__ == "__main__":
    solve()