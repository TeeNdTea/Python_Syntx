'''
1+2+3+....+n
2+4+6+....+n [sum of even numbers from 1 to n]
1+3+5+....+n    [sum of odd numbers from 1 to n]
4+8+12+....+n
1^2+ 2^2+ 3^2+....+n^2
2^2+ 4^2+ 6^2+....+n^2
1*2*3*....*n
1+1/2+1/3+....+1/n
'''

#1
# i=1
# n=int(input("Enter a number: "))
# count=0
# while i<=n:
#     count+=i
#     i+=1
# print(count)

#2
# sum=0
# n=int(input("Enter: "))
# for x in range(2,n+1,2):
#     sum+=x
# print(sum)

#3
# i=1
# sum=0
# n=int(input("Enter: "))
# while i<=n:
#     sum+=i
#     i+=2
# print(sum)

#4
# sum=0
# n=int(input("Enter: "))
# for x in range(4,n+1,4):
#     sum+=x
# print(sum)

#5
# i=1
# sum=0
# n=int(input("Enter: "))
# while i<=n:
#     sum+=i*i
#     i+=1
# print(sum)

#6
# i=2
# sum=0
# n=int(input("Enter: "))
# while i<=n:
#     sum+=i*i
#     i+=2
# print(sum)

#7
# i=1
# sum=1 #cant be 0
# n=int(input("Enter: "))
# while i<=n:
#     sum=sum*i
#     i+=1
# print(sum)

#8
sum=0
n=eval(input('Enter: '))
for x in range(1,int(n)+1,1):
    sum+=1/x
print(sum)