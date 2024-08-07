
def bastir(kere,tumce):
    i=0
    while i<kere:
        print(tumce)
        i+=1

tumce = str(input("Bir kelime girin: "))
kere = int(input("Kac kere basilsin: "))
bastir(kere,tumce)

def listeyeCevir(**params):
    return list(params.values())

Liste1 = listeyeCevir(name='Enes', surname='Bal', age=19)
Liste2 = listeyeCevir(name='Aycin', surname='Ak')
Liste3 = listeyeCevir(name='Ceylin', surname='Kara', age=35, dogumYili=1983)

print("Liste 1:", Liste1)
print("Liste 2:", Liste2)
print("Liste 3:", Liste3)

print("* "*20)
# Sectiginiz 2 sayi arasindaki asallari basar
def asalMi(sayi):
    if sayi < 2:
        return False
    elif sayi ==2:
        return True
    else:
        i=2
        while i<sayi:
            if sayi%i==0:
                return False
            else:
                return True
            i+=1

s1 = int(input("Sayi gir: "))
s2= int(input("Sayi gir: "))

for n in range(s1,s2):
    if asalMi(n):
        print(n)
    else:
        continue

print("* "*20)
# gonderilen sayinin bolenlerini basar
def bolenler(sayi):
    for i in range (1,sayi+1):
        if sayi % i == 0 :
            print(i)
        else:
            continue

sayi = int(input("SAyi girin: "))
bolenler(sayi)


