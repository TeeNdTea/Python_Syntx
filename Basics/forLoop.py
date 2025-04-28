num=[10,20,30,40,50]
# print(num)
#1
# idx=0
# while idx<=4:
#     print(num[idx])
#     idx+=1

#2. if length of list is not known
# idx=0
# n=len(num)
# while idx < n:
#     print(num[idx])
#     idx+=1

#3 using for loop

for x in num:       # x is a variable
    print(x)


#find sum using for loop

sum=0
for x in num:
    sum+=x
print(sum)