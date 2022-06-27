# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 01:09:41 2022

@author: erdog
"""

def split_digits_algorithm(value):
    thousand_digit = value / 1000
    hundred_digit = (value / 100) % 10
    ten_digit = (value / 10) % 10
    one_digit = value % 10
    
    print(int(thousand_digit), " ", int(hundred_digit), " ", int(ten_digit), " ", int(one_digit))
        
                        
def split_digits(value):
    #int(a) programa, for döngüsünün her turunda dönen a değerini listeye int tipinde eklemesini söylüyor.
    #list comprehension
    x = [int(a) for a in str(value)]
    print(x)
    

def split_digits2(value):
    import math
    x = [(value//(10**i))%10 for i in range(math.ceil(math.log(value, 10))-1, -1, -1)]
    print(x)
       
    
    
split_digits_algorithm(1045)
split_digits(204729)
split_digits2(6048123)