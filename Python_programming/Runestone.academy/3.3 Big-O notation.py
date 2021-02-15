# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:00:34 2021

@author: Komputer
"""

'''
Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). 
The second function should be linear O(n).

'''
# O(n) solution
def first_function(list):
    min=list[0]
    for i in range(1,len(list)):
        if list[i]<min:
            min=list[i]
    return min

first_function([2,3,5,8])

# O(n^2) solution
def second_function(list):
    for i in range(len(list)):
        is_min=True
        for j in range(len(list)):
            if j==i:
                continue
            else:
                if list[i]>list[j]:
                   is_min=False
        if is_min==True:
            return list[i]

               
first_function([10,3,5,-9,-1,-2])
second_function([-10,3,-9,8,-1,-2])