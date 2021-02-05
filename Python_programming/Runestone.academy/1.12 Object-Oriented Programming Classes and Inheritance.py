# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:22:18 2021

@author: Komputer
"""

class FractionCheck(Exception):
    
    def __init__(self,message="Nominator and denominator should be integers"):
        self.message=message
        super().__init__(self.message)

class Fraction:

    def __init__(self,top,bottom):
    
        if bottom<0 and top>0:
            self.num = - top
            self.den = - bottom
            
        else:
            self.num =  top
            self.den =  bottom
        
        
        if type(self.num)!=int or type(self.den)!=int:
            raise FractionCheck()
        
    
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def show(self):
     print(self.num,"/",self.den)
    #In Python, all classes have a set of standard methods. 
    #__str__ is the method to convert an object into string
  #  def __str__(self):
   #     return str(self.num)+"/"+str(self.den)
    
    def __repr__(self):
        return repr(self.num)+"/"+repr(self.den)
    
    #overloading of operator +
    def __add__(self,otherfraction):
        if type(otherfraction) in [int,float]:
            return otherfraction+self
        else: 
           newnum = self.num*otherfraction.den + self.den*otherfraction.num
           newden = self.den * otherfraction.den
           common = gcd(newnum,newden)
           return Fraction(newnum//common,newden//common)
   # a function to obtain deep equality
   #normally by default we have shallow equality (two objects of the class are eqaul
   #if they are references to the same object)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    #multiplication of two objects
    def __mul__(self,otherfraction):
        new_num=self.num*otherfraction.num
        new_den = self.den*otherfraction.den
        common=gcd(new_num,new_den)
        return(Fraction(new_num//common,new_den//common))
        
    def __sub__(self,otherfraction):
       newnum = self.num*otherfraction.den - self.den*otherfraction.num
       newden = self.den * otherfraction.den
       common = gcd(newnum,newden)
       return Fraction(newnum//common,newden//common)
   
    def __truediv__(self,otherfraction):
       newnum=self.num*otherfraction.den
       newden = self.den*otherfraction.num
       common = gcd(newnum,newden)
       return Fraction(newnum//common,newden//common)
          # // - floor division    
    def __gt__(self,otherfraction):
        newnum1=self.num*otherfraction.den
        newnum2=self.den*otherfraction.num
        if newnum1>newnum2:
            return True
        else:
            return False
        
    def __ge__(self,otherfraction):
        newnum1=self.num*otherfraction.den
        newnum2=self.den*otherfraction.num
        if newnum1>=newnum2:
            return True
        else:
            return False
        
    def __lt__(self,otherfraction):
        newnum1=self.num*otherfraction.den
        newnum2=self.den*otherfraction.num
        if newnum1<newnum2:
            return True
        else:
            return False
    
    def __le__(self,otherfraction):
        newnum1=self.num*otherfraction.den
        newnum2=self.den*otherfraction.num
        if newnum1<=newnum2:
            return True
        else:
            return False
          
            
        
    def __ne__(self,otherfraction):
        newnum1=self.num*otherfraction.den
        newnum2=self.den*otherfraction.num
        if newnum1!=newnum2:
            return True
        else:
            return False
#  adding number and instance of the fraction class
    def __radd__(self,other):
        return Fraction(int(other)*self.den + self.num, self.den)
# overloading of self+=number
    def __iadd__(self,number):
        return number + self
    
myfraction = Fraction(3,5)
myfraction.show()
print(myfraction)

f1=Fraction(1,-5)
f2=Fraction(1,4)
f3=f1+f2
print(f3)

f1>=f2
#Greatest Common Divisor - Euclid's Algorith
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

print(gcd(20,10))

print(f1==f2)
f3=f1*f2
print(f3)

# noninstance + instance
f=Fraction(1,2)
a=2
b=a+f
print(b)

c=f+a
print(c)

f+=2
print(f)

####################################################
#Inheritance

class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label
# performGateLogic is a virtual method. This is a method that will use code that does't exist yet.
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()
        
        
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
               raise RuntimeError("Error: NO EMPTY PINS")
   
        
class UnaryGate(LogicGate):
# calling a  constructor of parent class
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()
   
    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
    
class AndGate(BinaryGate):
#Python also has a function called super which can be used in place of explicitly naming the parent class.
#Useful when a class inherits from more than one parent class
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
   
class OrGate(BinaryGate):
#Python also has a function called super which can be used in place of explicitly naming the parent class.
#Useful when a class inherits from more than one parent class
    def __init__(self,n):
        super(OrGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0
        
class NotGate(UnaryGate):
    def __init__(self,n):
        super(NotGate,self).__init__(n)
    
    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1
     

# Creating circuit (connecting gates together)
#To do this we implement a new class called Connector
#It is called the HAS-A Relationship.

#Connector HAS-A LogicGate meaning that connectors will have instances of the LogicGate class within them
#but are not part of the hierarchy.

#HAS-A relationship = no inheritance

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    
    
        
        
a1 = AndGate("1")
a2 = AndGate("2")
a3 = OrGate("3")
a4 = NotGate("4")

#result from a1 goes to a3 as first parameter
c1=Connector(a1,a3)

#result from a2 goes to a3 as second parameter
c2 = Connector(a2,a3)

#result from a3 goes to a4 as parameter
c3 = Connector(a3,a4)

a3.getOutput()
a4.getOutput()
a2.getOutput()

