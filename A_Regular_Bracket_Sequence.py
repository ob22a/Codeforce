def solve():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())

    # str1= "(("
    # str2= "()"
    # str3= ")("
    # str4= "))"
    
    if cnt3>0 and (cnt1==0 or cnt4==0):
        print(0)
        return
    
    print(1 if cnt1==cnt4 else 0)

if __name__ == "__main__":
    solve()