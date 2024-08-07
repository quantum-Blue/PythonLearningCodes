
a = int(input('sayi girin: '))
if a<5:
    print('Hello World')

isLoggedin = True
if isLoggedin:
    print('Hello World')

if not isLoggedin:
    print('Hello World')

if isLoggedin == False:
    print('Hello World')

userName = 'Enes'
password = '1234'

isLoggedin = ( userName == 'Enes' ) & ( password == '1234' ) # & = and

if isLoggedin :
    print('Basarili bir sekilde giris yapildi')
else :
    print("Giris basarisiz")

name = "Howl"
password = "1234"
print(name,password)
if (name == "Howl"):
    print("isim dogru bir sekilde girildi ..")
    if (password == "12345"):
        print("Giris Basarili")
    else :
        print("Parola yanlis !! ")    
else :
    print("Isim hatali !!!. ")

# if name.lower() != 0 or len(password) < 7:
#     print ("Invalid Credentials!")
#     elif name[::-1] in ["owll", "wolleh"]:
# print ("Valid Credentials! Welcome to the system.")
# elif name[-1:] == "!":
# print ("You are an admin, welcome back!")

x = input("x : ")
y = input("y : ")

if x < y :
    print("x < y")
elif x == y : # else if in c++ !!
    print("x == y")
else :
    print("x > y")



import datetime
tarih = input("tarih girin (2004/15/7): ")
tarih = tarih.split('/')
print(tarih)

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafigeCikis
print(fark.days)
days = fark.days

if days <= 365 :
    print("1. Servis Araligini alabilirsiniz")
elif days > 365 and days <= 365*2 :
    print("2. Servis Araligini alabilirsiniz")
elif days > 365*2 and days <= 365*3 :
    print("3. Servis Araligini alabilirsiniz")
else :
    print("Servis araligi bitti !\n Hatali süre")
    

