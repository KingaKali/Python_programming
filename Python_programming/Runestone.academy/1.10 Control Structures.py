# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:37:44 2021

@author: Komputer
"""

import math

counter = 1
while counter <= 5:
    print("Hello world")
    counter+=1
    
for item in [1,3,6,2,5]:
    print(item)
    
wordlist=['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

A=set(letterlist)
B=list(A)
print(B)

n=4
if n<0:
   print("Sorry, value is negative")
else:
   print(math.sqrt(n))
   
if n<0:
   n = abs(n)
print(math.sqrt(n))

#List comprehension
sqlist=[x*x for x in range(1,11)]

sqlist=[x*x for x in range(1,11) if x%2 != 0]

[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']