# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:10:18 2018

@author: tbieleni
"""

#input("What's rolling:") eg.2D6

#for each i do randint(1,b)
#=+ outcome

from random import randint
def D2():
 return randint(1,2)

def D4():
 return  (randint(1,4))

def D6():
 return (randint(1,6))

def D8():
 return (randint(1,8))

def D12():
 return (randint(1,12))

def D20():
 return (randint(1,20))

#input("What's rolling?":)
#outcome = D6 
print(D6())