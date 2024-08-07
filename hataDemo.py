
liste = ["1","2","5a","10b","abc","10","50"]

def sayiMi(liste):
    for n in liste:
        if n.isdigit():
            print(n)

sayiMi(liste)


while True:
    sayi = str(input("sayi girin(!=q): "))
    if sayi == 'q':
            break
    try:
        result = float(sayi)
        print("Girdiginiz sayi: ",result)
    except ValueError:
        print("Gecersiz sayi !!")
        continue


def check_password(parola):
    for i in turkce_karakterler:
        if i in parola:
            raise TypeError("Parolada Turkce karakter var")
        else:
            pass
    print("gecerli parola girdiniz .d")

turkce_karakterler = ["ı","ö","ü","ç","ğ","ş"]
parola = input("parola: ")

check_password(parola)


def faktoryel(x):
    x=int(x)
    if x < 0:
        raise ValueError("Negatif deger")
    result = 1 

    for i in range(1,x+1):
        result *=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y = faktoryel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
