num = []
for i in range(int(input())):
    element = input()
    count = 0
    for j in range(0,len(element)): #iterate over the string
        res = element[j]
        if (element[j] == '4'):
            count+= 1
    num.insert(i, count)

print(*num, sep = "\n")    #Splat operator | Print list without loops | def valye sep = ' '
