# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 01:53:08 2022

@author: erdog
"""

import numpy #Karşılaştırmak için

def ekok_bul(self):
    çarpım = 1
    for i in self: çarpım *= i #Dizinin çarpımı
    for i in range(1, çarpım+1):
        if sum([i % j for j in self]) == 0:
            ekok = i
            print('Ekok', self, ':', ekok)
            break
        
        
def ebob_bul(self):
    for i in reversed(range(1, max(self))):
        if sum([j % i for j in self]) == 0:
            ebob = i
            print('Ebob', self, ':', ebob)
            break
        
        
ekok_bul([12, 14])
print('Modül Çıktısı:', numpy.lcm(12, 14))
dizi = [150, 24, 30, 48]
ebob_bul(dizi)
print('Modül Çıktısı:', numpy.gcd(150, [24, 30, 48]))