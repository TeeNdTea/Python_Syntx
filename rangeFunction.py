#generate a range of numbers; suppose 0-20

# range(10) - this will generate 0-9 output
#convert to list as list can hold multiple elements
# num=list(range(10))
# print(num)

#print a number at any index
# print(num[4])

''' print(range(10)) 
This representation tells you that the range object can produce numbers starting from 0 up to (but not including) 10.
inclusive-Includes the start and end points
exclusive- Includes the start point but excludes the end point

range function is exclusive
'''

# num1=list(range(5,11))  #include start and end point
# print(num1)

num2=list(range(2,51,5))    #start point, end point, interval(koto step jabe)
print(num2)