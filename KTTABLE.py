t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    moment_time  = list(map(int,input().split()))[:n]
    cooking_time = list(map(int,input().split()))[:n]
    for j in range(n):
        if(j==0):
            if(cooking_time[j] <= moment_time[j]):
                count += 1
        else:
            if(cooking_time[j] <= moment_time[j] - moment_time[j-1]):
                count += 1

    print(count)
