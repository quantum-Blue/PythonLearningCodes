array = 'one' , 2 , True , 4.5
print(array)
print(len(array))

user1 = ['User1' , 1]
user2 = ['User2' , 2]
users = user1 + user2
print(user1)
print(user2)
print(users)
print(users[1])
print(users[0])
a=users[1]
#print(a[0])
#print(users[1][0])

Cars = ['BMW' , 'Opel' , 'Mazda']
LengthCars = len(Cars)
print(Cars[0] + ' ' + Cars[2])
print(Cars[0] + ' ' + Cars[-1])

temp = Cars[0]
Cars[0] = Cars[2]
Cars[2] = temp

print(Cars)

Cars[1] = 'Nissan'
print(Cars)

result = 'Mercedes' in Cars
print(result)
# Cars dizisinde Mercedes bulunuyorsa True bulunmuyorsa False degerini dondurur

Cars[-2:] = ['Ferrari' , 'Honda']
result = Cars + ['Kia','Bugatti']
print(result)
del Cars[-1] # Cars in son elemanini siler
print(Cars)
print(Cars[::-1]) # Tersten yazdirir

numbers = [ 1 , 4 , 7 , 9 , 20 ]
Val1 = min(numbers)
Val2 = max(numbers)

letters = [ 'a' , 'f' , 'T' , 'k' ]
Char1 = min(letters)
Char2 = max(letters)

print(numbers[2:5])
print(letters[3:7])

numbers.append(37)
letters.append('V')
# append : sona eleman eklemesi yapar

numbers.insert( 4 , 89 )
# 4. elemani 89 sayisiyla degistirir (Alttaki dogru)
# Yer degistirmez o siraya elemani ekler
numbers.insert(len(numbers),28) # En sona 28 ekler
numbers.insert( -1 , 32 )
print(numbers)

letters.insert( 2 , 'P' )
# 2. elemani P harfiyle degistirir
print(letters)

numbers.pop() # Sondaki elemani siler
print(numbers)

numbers.pop(-3) # Sondan ucuncu elemani siler
print(numbers)

numbers.remove(4) # 4 sayisini diziden siler eger 4 yoksa hata verir
print( numbers)
letters.remove('T')
print(letters)

numbers.sort()
numbers.reverse()
# sort kucukten buyuge dogru siralar
# reverse ters cevirme islemidir
letters.sort()
letters.reverse()

print("numbers length : " + str((len(numbers))))
print("numbers length : " + str((len(letters))))

print(numbers.count(1))
print(letters.count('a'))
# Kac tane oldugunu gosterir

print(numbers)
print(letters)

result = 17 in numbers # 17 sayisi numbers icinde var mi diye kontrol eder
print(result) 
result = 'a' in letters # a harfi letters icinde var mi diye kontrol eder
print(result) 

numbers.clear()
letters.clear()
# clear dizinin tum elemanlarini siler
print(numbers)
print(letters)

str = "Fiat,Ford"
result = str.split(',')
print(result)

brand = [] # Bos bir array olusturduk
# brand : marka
mark = input("Mark : ")
brand.append(mark)
print(brand)


