
def sayHello():
    print("Hello")
sayHello()

def sayHello(name):
    print("Hello " + name)
sayHello("Enes")

def sayHello(name = 'User'):
    print("Hello " + name)
sayHello("Enes")
sayHello()

def sayHello(name):
    return "Hello "+ name
msg = sayHello("Enes")
print(msg)

def total(s1,s2):
    return s1 + s2
result = total
def total(s1,s2):
    return s1 + s2
result = total
print(total)
# print(total.__doc__)
# __doc__ belgelendirme yapar

def emekliligeNeKadarKaldi(age,name):
    """
    DOCSTRİNG: Dogum yiliniza gore emekliliginize kac yil kaldi
    İNPUT: Dogum yili 
    OUTPUT: Hesaplanan yil bilgisi
    """
    emeklilik = 64 - age
    if emeklilik > 0:
        print(f"{name} adli kisinin emekliligine {emeklilik} yil kaldi.")
    else:
        print(f"{name} zaten emekli oldu.")
emekliligeNeKadarKaldi(54,'Zeki')
emekliligeNeKadarKaldi(74,'Ayşe')

#print(help(emekliligeNeKadarKaldi))
# ustteki kod fonksiyonun icindeki yorum satirini basiyor
list = [1,2,3]
# print(help(list.append))
# append komutunun nasil calistigini anlatir
def add(a,b,c=0):
    return sum((a,b,c))
# sum 3 parametreyle calisir , hepsini toplar (galiba)
print(add(10,20))
print(add(10,20,30))

# tek tek parametrelerle ugrasmamak icin soyle yapilir
def add(*params): # tuple olmasi icin * kullandik
    return sum(params)
print(add(10,20,34))
print(add(10,20,36,78,43,12,87))

def add(*args):
    return sum(args)
print(add(10,20,34))
print(add(10,20,36,78,43,12,87))

def displayUsers(**args): # dictionary olmasi icin ** kullandik
    # dictionary : key , value
    for key,value in args.items():
            print(type(args))
            print("{} is {}".format(key,value))
displayUsers(name="Enes",age=19,city="Giresun")
displayUsers(name="Selin",age=76,city="Bolu",phone="1457658")
displayUsers(name="Murat",age=4,city="Bursa",phone="2565998",mail="asdf@gmail.com")

def myFunc(a, b , *args , **kwargs):
    print(a)
    print(b)
    print(*args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
myFunc(10,20,30,40,50,key1 = "value 1",key2="value 2")


# map methodu
def square(num):    return num**2
numbers=[1,3,5,9]
result =list(map(square,numbers))

result =list(map(lambda num: num**2 ,numbers))
# lambda kullanarak fonksiyona ihtiyac duymayiz
# daha dogrusu kendi fonksiyonunu olusturur

numbers = [1,3,5,9,10,4]
def check_even(num):    return num%2==0 
# sayi ciftse True , tekse False dondurur
result = list(filter(check_even,numbers))
result = check_even(numbers[2])




