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


#############################################################################################################
# Episode 2
#############################################################################################################

def new_salary(x):
    return x * 20 / 100 + x

null_list = []
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))
        
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]
        
#use list comprehension

#liste yazılırken sağdan sola doğru yazılır (genellikle)
[salary * 2 for salary in salaries] #[2000, 4000, 6000, 8000, 10000] - salaries elemanlarını 2 ile çarp
[salary * 2 for salary in salaries if salary < 3000] #[2000, 4000] - salaries elemanlarının 3000'den az olanları 2 ile çarp

#if-else birlikte kullanılacaksa sol tarafta belirtilmelidir, tek başına if kullanılacaksa sağ tarafta olmalıdır
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries] #[2000, 4000, 0, 0, 0] - salaries elemanları 3000'den küçük olanları 2 ile büyük olanları 0 ile çarp

#istediğimizi yaptırırken metot da çağırabiliriz
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries] #salaries elemanları 3000'den küçük olanlar için new_salary(salary * 2) büyük olanlar için new_salary(salary * 0.2) uygula 


#############################################################################################################

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

#Amaç: students listesinde stundes_no elemanları varsa isimlerini küçük harflere, yoksa büyük harflerle dönüştür

[student.lower() if student in students_no else student.upper() for student in students]
#['john', 'MARK', 'venessa', 'MARIAM']
#[student.upper() if student not in students_no else student.lower() for student in students] #2.yol


#######################
# Dict Comprehension
#######################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys() #key değerleri (k)
dictionary.values() #value değerleri (v)
dictionary.items() #key-value değerleri

{k: v ** 2 for (k, v) in dictionary.items()} #{'a': 1, 'b': 4, 'c': 9, 'd': 16}

{k.upper(): v for (k, v) in dictionary.items()} #{'A': 1, 'B': 2, 'C': 3, 'D': 4}

{k.upper(): v*2 for (k, v) in dictionary.items()} #{'A': 2, 'B': 4, 'C': 6, 'D': 8}


#############################################################################################################
# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.

numbers = range(10) #0'dan 10'a kadar değerler var
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
        
#use dict comprehension
#tek bir if yapısı olduğu için sağ tarafta
{n: n ** 2 for n in numbers if n % 2 == 0} #{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


#############################################################################################################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper()) #kalıcı değil


A = []

for col in df.columns:
    A.append(col.upper()) #kalıcı

df.columns = A


df = sns.load_dataset("car_crashes")

#use list comprehension
df.columns = [col.upper() for col in df.columns]


#############################################################################################################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

#step by step
[col for col in df.columns if "INS" in col] #['INS_PREMIUM', 'INS_LOSSES']

["FLAG_" + col for col in df.columns if "INS" in col] #['FLAG_INS_PREMIUM', 'FLAG_INS_LOSSES']

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]
"""
['NO_FLAG_TOTAL',
 'NO_FLAG_SPEEDING',
 'NO_FLAG_ALCOHOL',
 'NO_FLAG_NOT_DISTRACTED',
 'NO_FLAG_NO_PREVIOUS',
 'FLAG_INS_PREMIUM',
 'FLAG_INS_LOSSES',
 'NO_FLAG_ABBREV']
"""

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


#############################################################################################################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"] #veri seti içerisindeki sayısal değişkenleri seçmek için - O:object (kategorik değişken)
#['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses'] - sayısal değişkenler
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol - use list comprehension
new_dict = {col: agg_list for col in num_cols} #key değerlerini değiştirmiş oluyoruz, value sabit

#Ne işe yarar?
"""
listenin string ifadelerini [mean,min,max,sum] bunların aslında fonksiyon olduğunu anlayabilecek bir fonksiyon
yazarsak bu durumda bir değişkene otomatik olarak birden fazla fonksiyonu uygulayabiliriz
"""

df[num_cols].head() #sayısal değişkenleri seçtik 

df[num_cols].agg(new_dict) 
#agg fonk.'na bu şekilde sözlük göndererek sözlüğün içerisndeki değişkenlerin value bölümündeki bütün fonk'ları gidip bu değişkenlere otomatik olarak yapar
#değişkenlere bu şekilde liste içerisindeki fonksiyonlarımı uygulamış olduk