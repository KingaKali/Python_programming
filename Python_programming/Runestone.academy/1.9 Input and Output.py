# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:29:20 2021

@author: Komputer
"""

aName = input('Please enter your name: ')

aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))

print("Hello","World", sep="***")
print("Hello","World", end="***")

sradius = input("Please enter the radius of the circle ")
radius = float(sradius)
diameter = 2 * radius

age = int(input('Please enter your age: '))
print("%s is %d years old." % (aName, age))

print("%s is %20.2f years old." % (aName, age)) #Put the value in a field 20 characters wide with 2 characters to the right of the decimal point.
print("%s is %-20d years old." % (aName, age)) #Put the value in a field 20 characters wide, left-justified
print("%s is %020d years old." % (aName, age)) #Put the value in a field 20 characters wide, fill in with leading zeros.
