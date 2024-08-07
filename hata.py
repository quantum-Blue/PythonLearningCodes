
# error handling : Hata yonetimi


while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Hatali veri girdiniz.",ex)
    else:
        break
    finally:
        print("try except sonlandi")


'''
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except:
        print("Hatali veri girdiniz.")
    else:
        break
    finally:
        print("try except sonlandi")
'''


'''
except (ZeroDivisionError,ValueError) as e:
    print("Yanlis bilgi girdiniz")
    print(e)
'''

'''
except ZeroDivisionError:
    print("y icin 0 girilemez")
except ValueError:
    print("sadece sayi girebilirsiniz")
'''

# x=10
# if x > 5 :
#     raise Exception("x 5 den buyuk deger alamaz")

def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("paroşa en az 7 karakter olmalidir")
    elif not re.search("[a,z]",psw):
        raise Exception("parola kucuk harf icermelidir")
    elif not re.search("[A,Z]",psw):
        raise Exception("parola kucuk harf icermelidir")
    elif not re.search("[0,9]",psw):
        raise Exception("parola kucuk harf icermelidir")
    elif not re.search("[_,@,#]",psw):
        raise Exception("parola alpha numeric harf icermelidir")
    elif not re.search("[\s]",psw):
        raise Exception("parola bosluk icermemelidir")

# password = '123456'
# password = '12345678'
# password = '12345678A'
# password = '12345678Aa'
password = '12345678Aa_'

try:
    check_password(password)
except Exception as e:
    print(str(e)) 
else:
    print("gecerli parola : else")
finally:
    print("Validation tamamlandi")

class Person:
    def __init__(self,name,year):
        if len(name)<10:
            raise Exception("name 10 dan fazla karakter iceriyor")
        else:
            self.name=name
p = Person("Aliiiiiiiii",1989)



