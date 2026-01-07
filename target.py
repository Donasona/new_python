num=[1,3,5,4]
target=7
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print(num[i],num[j])