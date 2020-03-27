#from array import *
#import array

import array as arr
a = arr.array("i",[10,20,30,40])
c = arr.array("i",[1,2,3,4,5,6,7,8,9])

b = arr.array("d",[1.1,1.2,1.3,1.4,1.5])

print(a)
print()
print(b)
print()

# -------------append--------------------

a.append(2)

print(a)

#-------------extend---------------------

a.extend([5,6,7])

print(a)

#-------------pop--------(returns value)-

b = a.pop()
print(b)

#pop using index value
b = a.pop(2)
print(b)

#--------------remove--------------------

a.remove(5)
print(a)

#-------------insert uses indexing---------

a.insert(2,78)
print(a)


# array concatination----only work on same datatype array-----

d = arr.array("i")

d = a+c

print(d)

# array using for loop

for x in d:
    print(x)
    
print()


# array using while loop

x = 0
while x<d[5]:
    print(x)
    x+=1

print()

# while loop using len func -----

x = 0
while x < len(d):
    print(x)
    x+=1

