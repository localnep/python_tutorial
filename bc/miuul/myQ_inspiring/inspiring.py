#Denk geldiğim güzel sorular

values = [10, 30]
result = lambda values: [i if True in [True for j in range(2,10) if i % j == 0] else x for i, x in range(min(values), max(values))]
result(values)

########################################################################################################################

k = [2, 4, 6, 8, 10, 12]
l = [1, 3, 5, 7, 9, 11]
m = [3, 6, 2, 5, 1, 4]

def calculate(warm, moisture, charge):
    dict = {(i+1) : ((warm[i] + moisture[i]) / charge[i]) for i in range(0, len(k))}
    return dict

deneme = calculate(k, l, m)
print(deneme)
calculate(k,l,m)

########################################################################################################################

def calculate(warm, moisture, charge):
    calculated = {x[0]: ((x[1] + x[2]) / x[3]) for x in list(zip(list(*([range(1, len(warm)+1)])), warm, moisture,
                                                                 charge))}
    return calculated

calculate(k, l, m)

########################################################################################################################

a = ["ab", "cd", "ef"]
b = ["af", "ee", "ef"]

for i in range(len(a)):
    if len(set(a[i]).intersection(b[i])) == 0:
        print("NO")
    else:
        print("YES")

a = ["ab", "cd", "ef", "mm", "ab"]
b = ["af", "ee", "ef"]

set(a[0]).intersection(b[0]) # {'a'} - a[0] ile b[0] kesişimi
set(b[0]).difference(a[0]) # {'f'} - b[0] 'ın a[0]'dan farkı
set(a[3]) # {'m'} - a[3]'ün elemanı eşsiz olsun
set(a) # a listesi eşsiz olsun (sondaki 'ab' elemanı uçtu)

########################################################################################################################