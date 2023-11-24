# using list constractor 
my_list1 = list((1,2,3))
print(my_list1)

# using squre brackets[]
my_list2 = [1,2,3]
print(my_list2)

# using hetrogeneous items
my_list3 = [1.0,'jessa', 3]
print(my_list3)

# empty list using ## list() method
my_list4 = list()
print(my_list4)
var = []
print(var)

# lenth of a list ##  len()
list_len = [1,2,3,4,5,]
print(len(list_len))

# list indexing 
list_positive = [10,20, 'jenny', 30.50,'katrina']
print(list_positive[1])
print(list_positive[4])
# Negative indexing
list_negative = ["jenny", 40, 50.10, "katrina"]
print(list_negative[-2])
print(list_negative[-4])
print('---------------------')
# Iterate a list 
num = [5,8,'tom',2.20,'jenny']
for item in num:
    print(item)
print("______________________________")
# iterate along with an index number
list_num = [5,6,8,'jenny','tom',4.80]
for i in range(0,len(list_num)):
    print(list_num[i])  

# Adding element to the list ####  using 3 methods()
list_add  = list([3,1,"jenny","minny",5.40])
list_add.append("katrina")                        # append()
print(list_add)
list_add.append([23,45,67,"wow"])
print(list_add)
print('===========================')

# add item at the specified position in the list
list_add2 = list([1,6,'jenny','minny',8.90])
list_add2.insert(2, 45)                           # inssert()
print(list_add2)
list_add2.insert(4,['tom','jerry','wow'])
print(list_add2)
print("=============================")

# using extend()
add3 = list([2,5,7,'jenny',3.3])
add3.extend(["tom",56,'jerry'])
print(add3)
print('-------------------------------------')

# modifie the items of a list 
modify = list([2,3,4,5,8])
modify[0] = 20
print(modify)
modify[1:3] = [30,40,60]
print(modify)
modify[3:] = [80,100,120]
print(modify)
modify[-2:] = [150]
print(modify)

# modify all items
modify_all = list([2,3,4,5,6,8])
for i in range(len(modify_all)):
    square = modify_all[i] * modify_all[i]
    modify_all[i] = square
print(modify_all)
print("====================================")
# Removing elements from a list
l1 = list([1,3,2,4,5,6,7,8,])          # Remove specific item
l1.remove(4)
l1.remove(8)
print(l1)
print("===================")
list5 = list([5,4,5,5,5,8,12])
for item in list5:
    list5.remove(5)
print(list5)
# Remove item present at given index
l3 = list([1,3,4,5,8,6,9])
l3.pop(2)
print(l3)
l3.pop()        ##---pop()  last item remove
print(l3)
# Remove all items ----- clear()
l4 = list([2,3,5,1,7,8,9,6])
l4.clear()
print(l4)
del l4
print("========================")
# concatenation of two list  
my_l = [1,2,3,4]
my_l2 = [5,6,7,8,9]
my_l3 = my_l + my_l2
print(my_l3)
my_l.extend(my_l2) ### extend()
print(my_l)
print("================================")
### copying a list  ### copy()   
lc = [1,2,3]
new_lc = lc
print(new_lc)
lc.append(4)
print(lc)
print(new_lc)
### List using sort()
s = [5,6,4,3,7,9,8,2,1]
s.sort()                   #  sort()
print(s)
# Revers a list using 
r = [2,3,5,6,7,8,8]
r.reverse()
print(r)



















