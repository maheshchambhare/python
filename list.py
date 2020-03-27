
#list

fruit = ["apple","banana","mango"] #list is defined in square brackets

print(fruit)

fruit.append("cherry")

fav_fruit = fruit.copy() #copy
print(fav_fruit)


a = list(fruit)  #list
print(a)

#del fruit   #delete the list
#print(fruit)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)   #clears the list and return the value





#concadination of two list  (+)

fruit = ["apple","banana","mango"]
thislist = ["apple", "banana", "cherry"]

a = fruit + thislist

print(a)     


""" output   

['apple', 'banana', 'mango', 'apple', 'banana', 'cherry']

"""


# Indexing

print(a[2:5])   

#reverse the list

print(a[::-1])  # ['cherry', 'banana', 'apple', 'mango', 'banana', 'apple']

print(a[-1:0]) # []

print(a[:-1])  # ['apple', 'banana', 'mango', 'apple', 'banana']

print(a[-1])   # cherry




list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list2.extend(list1)
print(list2)

for x in list2:
  list1.append(x)

print(list1)



#constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist.insert ( 1 , "cherry")
print(thislist)

a = thislist.count("apple")
print(a)

b = thislist.pop()
print(b)
print(thislist)


c = thislist.remove("apple")
print(c)
print(thislist)


thislist.reverse()
print(thislist)



a = [100,28,15,440,5,6,17,8,29,10]
a.sort()
print(a)


"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""