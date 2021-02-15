# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 20:39:35 2021

@author: Komputer
"""

import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value
    # it will be useful to print the value of die without having to know about the instances
    #variable called current_value
    def __str__(self):
        return str(self.current_value)
    
    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)
    

my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()

#When we print a list of objects, the repr is used to display those objects
d_list = [MSDie(6), MSDie(20)]
print(d_list)