# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:51:37 2021

@author: Komputer
"""

import math
anumber = int(input("Please enter an integer "))
try:
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))
    

if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))
    

def square(n):
    return n**2

square(3)

#Newton's method for square root newguess=1/2∗(oldguess+n/oldguess)
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root

#‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.
#Program generating string and comparing it with the given one
# It keep letters that are correct and modify the rest
alphabet='abcdefghijklmnopqrstuvwxyz '
import random
def preparestring(strlen):
    res=''
    for i in range(strlen):
        res = res+ alphabet[random.randrange(27)]
    
    return res

preparestring(4)


def score(goal_string,my_string):
    score=0
    for i in range(len(goal_string)):
        if(goal_string[i]==my_string[i]):
            score+=1
    return score/len(goal_string)


def main():
    goal_string="kinga jest super"
    new_string=preparestring(len(goal_string))
    best=0
    newscore=score(goal_string,new_string)
    while newscore<1:
        if newscore>best:
            print(newscore,new_string)
            best=newscore
        new_string=preparestring(len(goal_string))
        newscore=score(goal_string,new_string)
        
main()
        