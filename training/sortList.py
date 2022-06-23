# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:03:41 2022

@author: erdog
"""

def sorting_algorithm(lis):
    
    temp = 0
    max_number = lis[0]
    min_number = lis[0]
    
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i] > lis[j]): #soldaki eleman sağdaki elemandan büyükse
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
        
    for i in lis:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i
    
      
    print(lis)                       
    print("min number: ", min_number, "max_number: ", max_number)
                
            
        

list1 = [30,15,45,35,20,25,10]
sorting_algorithm(list1)
#list1.sort()
#print(list1)
#print(max(list1))
#print(min(list1))