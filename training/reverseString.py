# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:29:58 2022

@author: erdog
"""

"""
*
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
For example: if the input string is "Hello World and Coders" 
then your program should return the string sredoC dna dlroW olleH.
Input: "coderbyte"
Output: etybredoc
Input: "I Love Code"
Output: edoC evoL I
"""

def reverse(input):
    str = ""
    for i in input:
        str = i + str
        #print(str)
    return str

def reverse2(input):
    return input[::-1]
 

str = input("enter a input string: ")

 
#print ("The reversed string(using loops) is : ",end="")
print (reverse(str))
print(reverse2(str))