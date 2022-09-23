t = int(input())
for i in range(t):
    res = 0
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    res = sum(1 for k in arr if k < 0)
    if(res % 2 == 0 or 0 in arr):
        print(0)
    else:   
        print(1)