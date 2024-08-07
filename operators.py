x,y,z = 3,5,10
print(x,y,z)
values = 1,3,5,7,9

#x, y, z = values
# print(x,y,z)
# ustteki kod hata verir cunku 3 degiskene 5 deger atamasi yapiyor ancak :
x, y, *z = values
print(x, y, z)
# Z nin icerisine 3 degisken girer ve bir liste olusturur
print(x, y, z[1])

#  print (x+y*2-z/4.0)**Tuple unpacking:**<jupyter_code># tuple unpacking:

numbers = 2 , 4 , 6 , 8
a , *b , c = numbers
print(a,b,c)

print('*'*50)

x=5
result = (x > 5) and (x < 10) 
print(result)

hak = 5
devam = 'e'
result2 = ( hak >= 4) and (devam == 'e') # && in c++
print(result2)

result = (x > 0) or (x % 2 == 0) # || in c++
print(result)

result = not(x > 0) # degilini alir

result = ( (x!=5) or (x<(-5)) and (x<97) )
print(result)

# if result is True:# if'den sonra parantezi yazmamiz gerekir

x = float(input('sayi gir: '))
result = x<100 and x>0
result = x>0 and (x%2==0)

x = y = [1,2,3] # x ve y ayni adres e sahip
z = [1,2,3] 
print(x==y) # True
print(x==z) # True
print(x is y) # True
print(x is z) # False
# icinde yazili elemanlar onemli degil 

del x[2]
y[1]=1
y.reverse()
print(x==y)
print(x is y)
print(x is not y)

# list comprehension:
# listelerde kopyalama yapmak istersek copy() fonksiyonunu kullanabiliriz
# listelerde kopyalama yaparken [] kullanilir
# print(id(x), id(y))

# Membership Operator: in

x = ['apple', 'banana']

print('banana' in x)

name = 'enes'
print('e' in name)
print('e' not in name)


