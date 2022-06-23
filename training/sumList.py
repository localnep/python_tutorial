# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:21:39 2022

@author: erdog
"""

"""
Input: ["[5, 2, 3]", "[2, 2, 3, 10, 6]"]
Output: 7-4-6-10-6
Input: ["[1, 2, 1]", "[2, 1, 5, 2]"]
Output: 3-3-6-2
"""

from itertools import zip_longest 

def sum_list(first,second):
     print(list(map(sum, zip_longest(first, second, fillvalue=0))))
     

def sum_list_algorithm(first,second):
    result = []
    
    if(len(first) == len(second)):
        result = ([x + y for x, y in zip(list1, list2)])
        
    else:
        #max_range = max(len(first),len(second))
        if(len(first) > len(second)):
            result = first
            for i in range(len(second)):
                result[i] = result[i] + second[i]
        else:
            result = second
            for i in range(len(first)):
                result[i] = result[i] + first[i]
                
   
    print(result)
        
        


list1 = [5, 2, 3]
list2 = [2, 2, 3, 10, 6]

list3 = [1, 2, 1]
list4 = [2, 1, 5, 2]

sum_list_algorithm(list1,list2)
sum_list_algorithm(list3, list4)