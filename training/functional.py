# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 22:25:01 2022

@author: erdog
"""

###############################################
# lambda, map, filter, reduce - functional programming - Vektör Seviyesinde İşlemler
###############################################

"""
lambda: Kullan at fonksiyonu, özellikle apply ve map ile birlikte kullanılır
map: Bir listedeki tüm ögelere bir fonksiyonu uygular. 
filter: “true” dönen elemanlar için bir liste oluştururken
reduce: genel olarak bir liste üzerinde işlemler yapmak için kullanılır.                                           
"""

def new_salary(x): #verilen maaş'a %20 zam yapar
    return x * 20 / 100 + x


#lambda
new_sum = lambda x: x * 20 / 100 + x


#map(function_name, list)
salaries = [1000, 2000, 3000, 4000, 5000]

list(map(new_salary, salaries))


#lambda - map use together
list(map(lambda x: x * 20 / 100 + x, salaries)) #salaries listesindeki elemanlara %20 zam yapar

#filter
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store)) # [2,4,6,8,10]

#reduce
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store) #list store'daki elemanları toplar