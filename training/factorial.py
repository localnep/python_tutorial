# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 01:50:06 2022

@author: erdog
"""

def factorial(num):
    result = 1
    
    if num == 0:
        return 1
 
    for i in range(num,0,-1):
        result *= i
    return result


def recursive_factorial(num):
    if num == 0:
        return 1
    
    else:
        return num * recursive_factorial(num-1)
    
    
def recursive_factorial2(num):
    return 1 if (num==1 or num==0) else num * factorial(num - 1)
    

number=int(input("enter a number: "))
print(factorial(number))
print(recursive_factorial(number))
print(recursive_factorial2(number))