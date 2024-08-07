
# file = open("newfile.txt","w") # w dosya olusturur ve yazar
# print(file)
# file.close()


# file =open("C:/Users/enesbal/Desktop/newfile.txt","w")
# print(file)
# file.close()


# file = open("newfile.txt","w")
# file.write("Tosun Paşa") # ş harfi sembol olur
# print(file)
# file.close()


# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Tosun Paşa") # ş harfi sembol olmamasi icin utf-8 yazilir
# print(file)
# file.close()


# file = open("newfile.txt","a",encoding='utf-8')
# file.write("Tosun Paşa") # Varolan dosyaya ekleme yapar ( yazma islemi)
# print(file)
# file.close()


# file = open("newfile.txt","x",encoding='utf-8') # x sadece dosya olusturur dosya mevcutsa hata verir
# file.close()


# file = open("newfile.txt","r+",encoding='utf-8') # r+ okuma ve yazimu

# file = open("newfile.txt",) # otomatik r olarak baslatir
# file.close()


# file = open("newfile.txt","r") # sadece okuma yapar
# file.close()


# file = open("newfile2.txt","r")
# print(file)
# FileNotFoundError hatasi verir 

# try:
#     file = open("newfile3.txt","r")
# except FileNotFoundError:
#     print("Dosya okunamadi !!")
# finally:
#     print("Dosya kapandi")   
#     file.close()


# file = open("newfile.txt","r",encoding='utf-8')
# for dongusu
# for i in file:
#     print(i)
# Araya bos satir koyarak cumleleri basar


# file = open("newfile.txt","r",encoding='utf-8')
# for i in file:
#     print(i,end="")
# Araya bos satir koyamadan cumleleri basar


# read
# file = open("newfile.txt","r",encoding='utf-8')
# print("icerik 1")
# content1 = file.read()
# print("icerik 2")
# content2 = file.read()
# file.close() 


# file = open("newfile.txt","r",encoding='utf-8')
# content=file.read(5)
# # ilk 5 karakteri alir
# content=file.read(3)
# print(content)
# file.close( )


# readline fonksiyonu
# Her seferinde tek bir satir okur
# file = open("newfile.txt","r",encoding='utf-8') 
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# file.close()
# en son yazili satira kadar basar ek satir eklemez
# end="" olmadan kullansaydik ilave satir eklerdi


# readlines fonksiyonu
# file = open("newfile.txt","r",encoding='utf-8') 
# liste = file.readlines
# print(liste)
# file.close()
# her satirdaki bilgiyi liste elemaninna cevirir
# print(liste[0])
# satir sayisini belirtmek icin indeks numarasina erismek mumkun


# with open("newfile.txt","r",encoding="utf-8") as file:
# # dosyayi acip okunmasini saglar ve snra kapatir
#     content = file.read()
#     print(content)
#     print(file.tell()) # imlecin klasorun hangi karakterinde oldugunu gosterir


# with open("newfile.txt","r",encoding="utf-8") as file:
#     content = file.read()
#     print(content)
#     file.seek(0) # imleci 0. karaktere goturur
#     print(file.tell())
 


# with open("newfile.txt","r",encoding="utf-8") as file:
#     content = file.read(10) # 10 karakter okur
#     print(content)
#     file.seek(5) # imleci 5. karaktere goturur
#     print(file.tell())
#     content2 = file.read(5) # 5 karakter okur
#     print(content2)


# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read() 
#     content = "Hallo Everyone\n" + content
#     print(content)
#     file.seek(0) 
#     file.write(content)
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


# with open("newfile.txt","r+",encoding="utf-8") as file:
#     list = file.readlines()
#     # help(list.insert)
#     list.insert(1,"Ali Korkmaz\n")
#     file.seek(0)
#     for i in list: # liste elemanlarini tek tek dolasark yapar bunun bir yolu daha var
#         file.write(i) 
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


# with open("newfile.txt","r+",encoding="utf-8") as file:
#     list = file.readlines()
#     list.insert(1,"Ali Korkmaz\n")
#     file.seek(0)
#     file.writelines(list )
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


