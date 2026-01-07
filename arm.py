num = 152
sum =0
temp = num
len = len(str(num))

while (temp >0):
    digit = temp%10
    sum+=digit**len
    temp//=10

if sum == num:
    print("no is arm")
else:
    print("no is not arm")