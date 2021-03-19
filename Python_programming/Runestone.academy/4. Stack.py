# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:05:26 2021

@author: Komputer
"""

class Stack:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
#The definition of the Stack class is imported from the pythonds module.
    
from pythonds.basic import Stack
s=Stack()

s.isEmpty()
s.push(2)
s.push(4)
s.pop()
s.peek()


'''
write an algorithm that will read a string of parantheses from left to right
and decide whether the symbols are balanced

Starting with an empty stack, process the parenthesis strings from left to right. 
If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. 
If, on the other hand, a symbol is a closing parenthesis, pop the stack. As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. 
If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly.

'''


def isbalanced(parantheses_string):
    s=Stack()
    balanced=True
    index=0
    while index < len(parantheses_string) and balanced:
        symbol=parantheses_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False
        index+=1
# the string is still balanced and stack was completely cleaned off
    if balanced==True and s.isEmpty():
        return True
    else:
        return False
    
def matches(open,close):
    openers="([{"
    closers=")]}"
    return openers.index(open)==closers.index(close)

isbalanced("(([]]))")


'''
Convert decimal number to its binary representation
Divide2 algorithm uses stack.
'''

def DivideByTwo(number):
    remainder_stack=Stack()
    while number >0:
        remainder_stack.push(number%2)
        number=number//2
       
    Binary_string=""
    while not remainder_stack.isEmpty():
        Binary_string=Binary_string+str(remainder_stack.pop())
        
    return Binary_string


result= DivideByTwo(230)
    
'''
Convert decimal number to its representation based on base value
DivideByBase algorithm uses stack.
Base can be between 2 and 16.
The remainders are pushed onto the stack.
For base beyond 10, we can't simply use the remainders, as they are themselves
represented as two-digit decimal numbers. Instead we need to create a set of digits that can be used to represent
those reminders beyond 9.
'''

def DivideByBase(number,Base):
    remainder_stack=Stack()
    digits = "0123456789ABCDEF"
    while number >0:
        remainder_stack.push(number%Base)
        number=number//Base
       
    Binary_string=""
    while not remainder_stack.isEmpty():
        Binary_string=Binary_string+digits[remainder_stack.pop()]
        
    return Binary_string


result= DivideByBase(26,26)

                