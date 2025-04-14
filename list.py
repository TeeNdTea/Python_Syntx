# my_list = ['apple','banana','mango','litchi']
# print(my_list)
# print(my_list[2]) #accessing + printing index
# print(my_list[1:])  #idx 1 theke bki shb
# print(my_list[-1])  #reverse print idx

#check if an item is in the list
# print('python' in my_list)
# print('Litchi' in my_list) # python is case sensitive language
# print('swift' not in my_list)

#adding elements in list
# print(my_list + ['kotlin',20,30.6])

# multiplying a list
# print(my_list * 2)


# P A R T 2:     F U N C T I O N S

# l=['php','java','python','kotlin']
# print(len(l))   #length of list
# l.append('JS') # adding an element to list

# l.insert(2,'swift') # inserting an element at any index

# l.remove('php') #removing an element

# l.sort() # cannot sor different data types...int string[alphebatic order]

# print(l)

p=[201,46,89,19,89,45,89]
# p.reverse()
# p.pop() # last item not print
#p.clear()
# p1=p.copy()
# print(p1)
# print(p.index(201)) #find index of an element
print(p.count(89))  #to count how many times an element is in list
