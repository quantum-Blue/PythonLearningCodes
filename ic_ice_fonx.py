# encapsulation

# def us_alma(number):
#     def inner(power):
#         return number ** power
#     return inner
# two=us_alma(2)
# three=us_alma(3)
# print(two(3))
# print(three(4))


# def yetki_sorgula(page):
#     def inner(role):
#         if role=="admin":
#             return "{0} rolunun {1} sayfasina ulasabilir".format(role,page)
#         else:
#             return "{0} rolunun {1} sayfasina ulasamaz".format(role,page)
# user1=yetki_sorgula("Product Edit")
# print(user1("admin"))


# def islem(islem_adi):
#     def toplam(*args):
#         toplam=0
#         for i in args:
#             toplam+=i
#         return toplam
#     def carp(*args):
#         carpim=1
#         for i in args:
#             carpim*=i
#         return carpim
#     if islem_adi == "toplam":
#         return toplam
#     elif islem_adi =="carp":
#         return carp
# toplam = islem("toplam")
# print(toplam(1,2,3,4,44,123))
# carp = islem("carp")
# print(carp(5,6,7,8))


# def toplam(a,b):
#     return a+b
# def cikarma(a,b):
#     return a-b
# def bolme(a,b):
#     return a/b
# def carpma(a,b):
#     return a*b
# def islem(f1,f2,f3,f4,islem_adi):
#     if islem_adi=="toplam":
#         print(f1(2,4))
#     elif islem_adi=="cikarma":
#         print(f2(9,3))
#     elif islem_adi=="bolme":
#         print(f3(10,2))
#     elif islem_adi=="carpma":
#         print(f4(5,6))
#     else:
#         print("gecersiz islem ...")
# islem(toplam,cikarma,bolme,carpma, "toplam")        
# islem(toplam,cikarma,bolme,carpma, "cikarma") 
# islem(toplam,cikarma,bolme,carpma, "bolme") 
# islem(toplam,cikarma,bolme,carpma, "carpma")
# islem(toplam,cikarma,bolme,carpma, "carpmaaa")
# islem(toplam,cikarma,bolme,carpma, "gecersiz")


# decorators

# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyonlardan onceki islemler")
#         func(name)
#         print("fonksiyonlardan onceki islemler")
#     return wrapper
    
# @my_decorator # sayHello'u my_decorator'a gonderir
# def sayHello(name):
#     print("hello ",name)

# sayHello("Enes")
###
# def sayGreeting():
#     print("greeting")

# sayHello=my_decorator(sayHello)
# sayHello()

# sayGreeting=my_decorator(sayGreeting)
# sayGreeting()


# print("* "*20)

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+func.__name__+" "+str(finish-start)+"saniye surdu")
    return inner

@calculate_time
def usalma(a,b):

    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
    
@calculate_time
def toplam(a,b):
    print(a+b) 

usalma(2,3)
faktoriyel(4)
toplam(4,67)
