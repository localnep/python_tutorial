# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def is_prime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0: #number will only be divided by itself
            count+=1
    if count==1:
        print (n, " is prime number")
    else:
        print (n," is not prime number")
        
        
def is_prime2(n):
    for i in range(2,n):
        if (n%i)==0:
            return False    
    return True
 
    
number=int(input("enter a number: "))

is_prime(number)

for i in range(2,number+1):
    if(is_prime2(i) == True):
        print(i," ")
        
##################################################################################################################        
        
values = [10, 30] #range of values
result = lambda values: [i for i in range(min(values), max(values)) if True in [True for j in range(2,10) if i % j == 0]]
result(values)