'''
*
**
*** n=3
'''

# n=4
# for i in range(1,n+1):
#     print(i*'*')

'''
*
***     (2*i-1)
*****
'''

# n=3
# for i in range(1,n+1):
#     print((2*i-1)*'*')

'''
    *
   **
  ***            i represents the current line number being printed.
 ****        space*(n-i) + ('*'*i) [i=1...5-1=4]
*****
'''
# n=5
# for i in range(1,n+1):  #height initialize
#     print(' '*(n-i)+'*'*i)

'''
*****
****
***
**
*       
'''

# n=5
# for i in range(n,0,-1):
#     print('*'*i)

'''
    *
   ***
  *****
 *******
*********
(2*i-1)* '*'*i
space n-i
'''
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i) + (2*i-1)*'*')

'''
*********       i=5
 *******        i=4               
  *****     total no,n is same which is 5
   ***      but i,line no. is changing
    *
'''
# n=5
# for i in range(n,0,-1):
#     print(' '*(n-i) + (2*i-1)*'*')

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
# n=5
# for i in range(1,n+1):
#     print(' '*(n-i) + (2*i-1)*'*')
# for j in range(n-1,0,-1):
#     print(' '*(n-j) + (2*j-1)*'*')

'''
****
****
****
****
'''
# n=4
# for i in range(n):
#     print('*'*n)

'''
    *
   ***
  *****
 *******
*********
*********
*********
*********
*********
'''
n=5
for i in range(1,n+1):
    print(' '*(n-i) + (2*i-1)*'*')
for j in range(n-1,0,-1):
    print(' '*(n-i) + (2*i-1)*'*')