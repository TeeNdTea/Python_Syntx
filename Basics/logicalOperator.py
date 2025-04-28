''' 
and[all cond needs to be true] 
or[only one needs to be true] 
not[]'''
num1=23
num2=34
num3=78

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

#vowel consonent