# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:17:53 2021

@author: Komputer
"""

# In python everything is given by the reference.
#A isa pinter to myList**3 so changing myList changes A
myList = [1,2,3,4]
B=myList*3
print(B)
A = [myList]*3
print(A)
myList[2]=45
print(A)

## Operation on lists
myList.append(2)
myList.insert(3,55)
myList.pop(3)
myList.pop()
myList.sort()
myList.reverse()
del myList[1]
myList.index(2)
myList.count(2)
myList.remove(2)


# range produces a range object that represents a sequence of values

range(0,10)
list(range(0,10))
list(range(5,10,2))
list(range(10,1,-2))

## Strings
#A major difference between lists and strings is that lists can be modified while strings cannot. 

myName="Kinga"
myName[3]
len(myName)

myName.upper()
myName.center(10)
myName.find('a')
myName.split('g')

myName.count('i')


## Tuples
#Tuples are very similar to lists in that they are heterogeneous sequences of data. The difference is that a tuple is immutable, like a string. 

myTuple = (2,True,4.96)
len(myTuple)
myTuple[0:2]


# Sets
#A set is an unordered collection of zero or more immutable Python data objects.
# Sets don't allow  duplicates 

mySet = {3,6,"cat",4.5,False}
len(mySet)
False in mySet

yourSet={99,3,100}
mySet.union(yourSet)

mySet | yourSet #Returns a new set with all elements from both sets

mySet.intersection(yourSet)
mySet & yourSet

mySet.difference(yourSet)
mySet - yourSet

{3,100}.issubset(yourSet)

{3,100}<=yourSet #Asks whether all elements of the first set are in the second

mySet.add("house")
mySet.remove(4.5)
mySet.pop()
mySet.clear()


# Dictionary
#Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. 

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))


for k in capitals:
   print(capitals[k]," is the capital of ", k)

# The dictionary is maintained in no particular order with respect to keys.
#The placement of the key is dependent on the idea of "hashing".
   
phoneext={'david':1410,'brad':1137}
phoneext.keys()
phoneext.values()
phoneext.items()
phoneext.get("kent")
phoneext.get("kent","NO ENTRY") #Returns the value associated with k, no entry otherwise