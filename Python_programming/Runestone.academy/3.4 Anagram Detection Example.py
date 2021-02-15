# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:39:39 2021

@author: KingaKali
"""

'''
 O(n^2) Comparing two strings - if the string2 contains the letter from
 string1 then put None in the placement of this letter in the list
 created from first string.
 
 Remember - string is immutable - you need to create a list of letters from string
'''
def AnagramSolution1(s1,s2):
    OK=True
    if len(s1)!=len(s2):
        OK=False
    
    s1=s1.upper()
    s2=s2.upper()
    
    s1_list=list(s1)
    position2=0
    
    while position2<len(s2) and OK:
        position1=0
        found=False
        
        while position1<len(s1) and not found:
            if s2[position2]==s1_list[position1]:
                found=True
            else:
                position1+=1
            
        if found:
            s1_list[position1]=None
        else:
            OK=False
                
        position2+=1
        
    return OK
'''
It depends on the type of sorting (n^2 or nlogn)
O(nlogn) - MergeSort in function sorted 
- sorting and comparing
'''
def AnagramSolution2(s1,s2):
    
    s1=sorted(list(s1.upper()))
    s2=sorted(list(s2.upper()))
    
    if len(s1)!=len(s2):
        return False
    else:
        return s1==s2

from itertools import permutations  

'''
 O(n!) solution
Generating all possibilities of strings based on letters from first string
and checking if second string is in this list
'''
def BruteForce(s1,s2):
    s1_list=list(s1.upper())
    perm=permutations(s1_list)
    list_of_strings=[]
    for p in list(perm):
        list_of_strings.append(list(p))
    
    if list(s2.upper()) in list_of_strings:
        return True
    else:
        return False
    
'''
O(n) solution
Anagrams will have the same number of each letter

In Python, the ord() function accepts a string of unit length as an 
argument and returns the Unicode equivalence of the passed argument. 
T(n)=2n+26 (as we have 26 possible characters in the string)

Since Python 3.6 dictionaries are ordered.
Dictionary is a hash mapping/hash table. 
'''
def Count_and_Compare(s1,s2):
    
    c1=[0]*26
    c2=[0]*26
    
    s1=s1.upper()
    s2=s2.upper()

    for i in range(len(s1)):
        position = ord(s1[i])-ord('A')
        c1[position]+=1
        
    for j in range(len(s2)):
        position = ord(s2[j])-ord('A')
        c2[position]+=1
        
    return c1==c2
        
       
def Count_and_Compare_with_dictionary(s1,s2):

    c1=dict((el,0) for el in range(26))
    c2=dict((el,0) for el in range(26))
    
    s1=s1.upper()
    s2=s2.upper()
    
    for i in range(len(s1)):
        position = ord(s1[i])-ord('A')
        c1[position]+=1
        
    for j in range(len(s2)):
        position = ord(s2[j])-ord('A')
        c2[position]+=1
        
    return c1==c2
    
    
print(AnagramSolution1("dAca","baDa"))
print(AnagramSolution2("dAba","baDa"))
print(BruteForce("dAba","baca"))
print(Count_and_Compare("appke","pleap"))
print(Count_and_Compare_with_dictionary("apple","pleap"))



