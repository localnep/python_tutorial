# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 01:15:47 2022

@author: erdog
"""

#List Comprehension [expression for item in list]

isimler = ["Ahmet","ali","Çınar","DeNiz"]
string = "Hello 12345 World"
yillar = [1983, 1999, 2008, 1956, 1968]
dereceler = [20,5,15,-2,0,-6]

#1: "1-100" arasındaki sayılardan 12'e tam bölünebilen sayı listesi oluşturunuz.

sonuc = [i for i in range(1,101) if i%3==0 if i%4==0]

#2: isimler listesindeki her ismi küçük harfe çevirip tersten yazdırınız.

sonuc = [i.lower()[::-1] for i in isimler]

#3: verilen string içindeki rakamları içeren bir liste oluşturun.

sonuc = [i for i in string if i.isdigit()]

#4: "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturun.

import datetime
simdi = datetime.datetime.now().year #şuan ki yıl bilgisi getirilecek
sonuc = [simdi - yil for yil in yillar]

#5: "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesini yazınız.

sonuc = [i if i>0 else "buzlanma tehlikesi" for i in dereceler]

    
print(sonuc)