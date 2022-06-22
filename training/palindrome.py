# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:48:34 2022

@author: erdog
"""

"""
Palindromik sayı ve kelime, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılar ve kelimelerdir.
Örnek: 1, 4, 8, 99, 101, 363, 4004, 1221, 9889 vb.
örnek: kazak,neden,yatay,racecar
"""

def isPalindromeString(input):
    
    reverseString = input[::-1]
    
    if(input == reverseString):
        print("The string is a palindrome")
    
    else:
        print("Not a palindrome")
        

def isPalindromeNumber(num):
    
    temp = num
    rev = 0
    
    while(num>0):
        dig=num%10
        rev=rev*10+dig 
        num=num//10       
    
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
    
    

str = input("enter a input string: ")
isPalindromeString(str)

value = int(input("enter a number: "))
isPalindromeNumber(value)