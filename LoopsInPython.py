import setuptools


numbers = [ 1,2,3 ]
# for i in range(len(equals)):
for num in numbers:
    print(num)

names = ["Enes" , "Emre" , "Efe"]
for name in names:
    print(f"my name is {name}")

name = "Za Warudo"
for n in name:
    print(n)

tuple = [(1,3),(2,4),(5,7)]
for t in tuple:
    print(t)
for a,b in tuple:
    print(a,b)
for a,b in tuple:
    print(a)

d = { 'k1':3 , 'k2':2 , 'k3':45 }
# k1 = key , 3 = value

for item in d:
    print(item) # sadece key bilgilerini yazdirir
for item in d.items():
    print(item) # tamamini basar
for key,value in d.items():
    print(key)
for key,value in d.items():    
    print(value)


sayilar = [1,3,5,7,9,12,19,21]
print(sayilar)
print("3 e bolunebilenler :")
for n in sayilar:
    if (n%3==0):
        print(n)

toplam =0
for n in sayilar:
    toplam +=n
print(f"Sayilarin toplami : {toplam}")

for n in sayilar:
    if(n%2==1):
        print(f"sayi : {n} , sayinin karesi : {n**n}")
sehirler = [ "kocaeli" , "istanbul" , "ankara" , "izmir" , "rize" ]
# sehirlerden hangileri en fazla 5 karakterlidir
for city in sehirler:
    if len(city)>=5:
        print(city)

# Urunlerin icinden tutarı 5k nin altindakilerin ismini yazdirin
urunler = [
        {'name':'samsung s6', 'price' : '3000'} ,
        {'name':'samsung s7', 'price' : '4000'} ,
        {'name':'samsung s8', 'price' : '5000'} ,
        {'name':'samsung s9', 'price' : '6000'} ,
        {'name':'samsung s10', 'price' : '7000'}
]
print(urunler)
toplam = 0
for urun in urunler:
    toplam += int(urun['price'])

print("Toplam fiyat:", toplam)

print("Urunlerin listesi (5000 TL'den dusuk olanlar):")
for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name'])
# Bu kod, her ürünün fiyatını doğru bir şekilde toplar 
# Ve ardından 5000 TL'den düşük olan ürünleri ekrana yazdırır.

#   While Loops (While Donguleri)
# while loopları asla sonlandırmayın! Bunun için break kullanınız.
while True: # Herhangi bir koşul sağlayan durumda çalışacaktır.
    print("Merhaba Kullanici ! ")
    # Eğer kullanıcıdan girdi almak istiyorsanız input fonksiyonunu kullanabilirsiniz.
    #    name=input('Adiniz:')
    # Burada klavye ye girilen verilere baska islemler gerceklestirebilirsiniz.
    break
# Bir programdaki tüm komutların tek satırı olması gerekir.
'''
x = 0
while True:
    print(x) # Sonsuz dongu
'''

x=0
while x < 45:
    print(x)
    x+=5

name = '' # False
while not name.strip(): # Isim girerken bosluk girmememizi saglar
    name = input("isminizi girin: ")
print(f"Merhaba, {name}")

# Blackbox in ufak Tuyolari .d
"""
# For Looplar ile Listelerdeki Verileri İncelemek ve Değiştirmek
names=['ali','veli','hasbi']
for i in names:
    if len(i)>2 and "v" in i[::]:
        print(len(i))
"""

sayilar = [1,3,5,7,9,12,19,21]
i = 0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1

baslangic = int(input("baslangic: "))
bitis =  int(input("bitis: "))

i=baslangic
while i< bitis :
    if i%2==0:
        i+=1
        print(i)
i=10    
while i>0:
    print(i)
    i-=1
numbers = []
i=0
while i< 5:
    sayi = int(input("sayi: "))
    numbers.append(sayi)
print(numbers)
numbers.sort()
print(numbers)

urunler = []
adet = int(input("Adet girin: "))
i = 0
while i < adet:
    name = input("urun ismi: ")
    price = int(input("urun ismi: "))
    urunler.append({
        'name': name , 
        'price':price
    })
    i+=1
for  urun in urunler:
    print(f"Urunun adi: {urun['name']} , Urunun fiyati: {urun['price']} ")

#   BREAK CONTİNUE
name = 'enes'
for letter in name:
    if letter == n:
        break
    print(letter)
for letter in name:
    if letter == n:
        continue
    print(letter)

#    LOOP OPERATORS

# 1- range()
list = [1,2,3]
for item in list: # Elemanlariyla birlikte tanimlanmis bir listeyi yazdirir
    print(item)

for item in range(10): # 10 a kadar olan sayilari basar
    print(item)

for item in range(3,10): # 3 ten 10 a kadar olan sayilari basar 
    print(item)

for item in range(5,75,10): # 5 ten 75 e kadar 10 ar 10 ar sayilari basar 
    print(item)

print(list(range(5,75,10))) # Az onceki donguyu listeye cevirir

# 2- enumerate
greetings = 'Hello There'
index = 0
for letter in greetings:
    print(f"index: {index} , letter: {letter}")
    index+=1

for letter in greetings:
    print(f"index: {index} , letter: {greetings[index]}")
    index+=1

for index,letter in enumerate(greetings):
    print(f"index: {index} , letter: {letter}")
    index+=1

for item in enumerate(greetings): # Otomatik olarak her harfin index numarasiyla basar
    print(item)

# 3- zip
list1 = [1,2,3,4]
list2 = ['a', 'b', 'c', 'd']
list3 = [10,20,30,40]
print(list(zip(list1, list2, list3))) # Liste 1 ve 2 yi birlestirir

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)


numbers = [x for x in range(10)]
# x e 10 a kadar olan sayilari atar
# Sonra x i numbers a atar (array)
print(numbers)

numbers = [] # Bir dizi tanimladik
for item in range(10):
    numbers.append(item)
print(numbers)


for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x%3==0]
print(numbers)

myString = 'hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

years = [ 1983 , 1999 , 2008 , 1956 , 1986]
ages = [2023 - year for year in years]
print(ages)

result = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)

result = []

for x in range(3):
    for y in range(5):
        result.append((x,y))
print(result)

numbers = [(x,y) for x in range(5) for y in range(3)]
print(numbers)

numbers = [(x,y,z) for x in range(2) for y in range(2) for z in range(2)]
print(numbers)



