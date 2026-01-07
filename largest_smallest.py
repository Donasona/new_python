num=[2,1,5,4,3,6,7,8,2,12]
sort=sorted(set(num))
if len(sort)>=2:
   smallest_num=sort[2]
   largest_num=sort[-3]
print("the smallest num:",smallest_num)
print("the largest num:",largest_num)