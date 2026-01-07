num=int(input("enter the number:"))
sum=0
for digit in str(num):
    sum+=int(digit)
if num%sum==0:
    print("Harshad number")
else:
    print("not a harshad number")