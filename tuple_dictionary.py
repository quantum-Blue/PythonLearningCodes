#       List & Tuple
list = [1, 2, 3, 4]

# tuple = 1 , 'iki' , 3.4
# Ustteki veya alttaki sekilde kullanilabilir
tuple = (1 , 'iki' , 3.4)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list[2]))
print(len(tuple[2]))

list = ['ali' , 'veli']
tuple = ('damla' , 'ayse' , 'ayse')

print(list)
print(tuple)

list[0] = 'ahmet'
tuple[0] = 'deniz'

print(list)
print(tuple)
# tuple nin elemanlarinin atamasi yapildiktan sonra degistirilemez
# tuple de sadece index ve count method lari kullanilir

print(tuple.count('ayse'))
print(tuple.index('ayse'))

print('- - - - - - - - - - - - - - - - - - - - -')

#       Python'da Dictionary
sehirler = ['Giresun' , 'İstanbul']
plakalar = [28 , 34]

print(plakalar[sehirler.index('Giresun')])

# 2 tane liste yazmak yerine bunu tek adimda yapabiliriz
# plakalar = { 'key' : 'Value' }
plakalar = { 'Giresun' : 28 , 'İstanbul' : 34 }
print(plakalar['Giresun'])
print(plakalar['İstanbul'])
print(plakalar)

plakalar['Ankara'] = 6
plakalar['Istanbul'] = 'new value'
print(plakalar)

del plakalar['Giresun'] # delete key
print(plakalar)

users = {
    "1": {"name":"Enes", "surname":"Bal", "age":19, "roles":["admin","user"]},
    "2": {"name":"Muhammed", "surname":"Ali", "age":56, "roles":["user"]}
}

print(users['1'])
print(users['1']['name'])
print(users['1']['roles'])
print(users['1']['roles'][0])
print(users['2'])
print(users['2']['surname'])
print(users)
 
students = {}
number = input("student no: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("tel: ")

students[number] = {
    'name' : name ,
    'surname': surname ,
    'tel'   : phone ,
    }
print(students)

students.update({
    number: {
        'ad' : name ,
        'soyadi' : surname ,
        'tel' : phone
    }
})
print(students)

ogrNo = input('ogrenci no: ')
student = students(ogrNo)
print(student)

print('*'*50)

print(f"Aradiginiz  {ogrNo} nolu ogrencinin adi : {student['name']} soyadi : {student['surname']} ve telefonu {student['phone']}")

print('*'*50)
#Python'da Sets

fruits = {'orange', 'apple', 'banana'}
# Suslu parantez icine yazilir , index lenemezler. 
# print(fruits[1])   hata verir

for x in fruits:
    print (x)
# liste elemanleri dongu yardimiyla yazdirilir ancak siralanamaz

fruits.add('cherry')
print(fruits)
fruits.update(['mango', 'grape', 'apple'])
print(fruits)
# Apple zaten icerde de oldugundan elemanlar tekrarlanmaz
# Listenin icerisinde her elemandan sadece 1 tane olur
fruits.remove('mango') # Mango yu listeden siler
fruits.discard('apple') # Apple i listeden siler
del fruits['banana']    # Bananani listeden silmek istersek del kullanabiliriz
fruits.pop() # Fruits sirali dizi olmadigindan rastgele eleman siler


# Listelerdeki gibi sette de for ile cagirmaya da gerek kalmayacaktır
fruits2=set() # boyle bir sekillenme yapilabilir
fruits3={'apple','orange','banana'}
fruits4={1,2,'apple'}
print(type(fruits))    #<class 'set'>
print(len(fruits))     # 3
print(fruits & fruits2)# {}
print(fruits | fruits2)# {'banana', 'apple', 'orange'}
print(fruits - fruits2 )#{'banana', 'orange'}
print(fruits ^ fruits2 ) #{'banana', 'orange', 'apple'}

fruits.clear()
fruits2.clear()
fruits3.clear()
fruits4.clear()

