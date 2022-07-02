# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 19:14:51 2022

@author: erdog
"""

#############################################################
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
#############################################################
def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)
    

#main
alternating("hi my name is john and i am learning python")


#######################################################
#Enumerate -> Bir iteratif nesne içerisinde gezip elemanlarına birşey yaparken aynı zamanda o elemanların index bilgilerini takip etmek istediğimizde
#######################################################

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []] #2 alt listeyi içeren groups listesini return edeceğiz
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]


#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

#main
alternating_with_enumerate("hi my name is john and i am learning python")


#######################
# Zip -> #farklı listeleri, eşlemek, birbiriyle değerlendirmek istiyoruz
#######################


students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages)) #bir liste içerisinde tuple formunda