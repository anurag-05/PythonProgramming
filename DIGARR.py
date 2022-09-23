for i in range(int(input())):
    flag = False
    n = int(input())
    str = input()[:n]
    for j in range(0,len(str)):
        if (str[j] == '5' or str[j] == '0'):
            flag = True
            break
    if(flag):
        print("Yes")
    else:
        print("No")        