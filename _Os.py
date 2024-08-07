# DOSYA ADİ KUTUPHANE ADİYLA AYNI OLAMAZ
import os
import datetime

result=dir(os)

print(result)

result = os.name
print("OS name is: ", result)
# Hangi isletim sistemini kullandigini gosterir

result = os.getcwd()
print("Current working directory :", result) # Acik dizinin pc de nerede bulundugunu gosterir
os.mkdir("newdirectory") # Ayni dizin icine yeni klasor olusturur
print(result)

os.chdir("C:\\") # dizin degistirir
os.chdir("..") # Bir ust dizine gecer
os.chdir("../..") # 2 kere ust klasore gecer

os.makedirs("newdirectory/yeniklasor") # Klasor olusturur , ic ice fln 
# newdirectory (ust) -> yeniklasor (alt)

result = os.listdir() # Aktif olan dizinin icindeki klasorleri gosterir
print(result)

result = os.listdir("C:\\") 
print(result)

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

result=os.stat("files.py") # Dosya hakkinda bilgi verir
print(result)
result=result.st_size # byte cinsinden dizinin kapladigi alani verir
print(result)
result=result.st_ctime # 
print(result)
result = datetime.datetime.fromtimestamp(result.st_ctime) # dosyanin olusturulma tarihini gosterir
print(result)
result = datetime.datetime.fromtimestamp(result.st_atime) # dosyanin son erisilme tarihini gosterir (axess)
print(result)
result = datetime.datetime.fromtimestamp(result.st_mtime) # dosyanin son degistirilme tarihini gosterir (modified)
print(result)

os.system("notepad.exe") # notepad uygulamasini acar

os.rename("newdirectory","yeniklasor") # newdirectory klasorunun adini yeniklasor olarak degistirir
os.rmdir("newdirectory") # newdirectory klasorunu siler
os.removedirs("newdirectory/yeniklasor") # newdirectory altindaki yeniklasor u siler (klasorun ici bos olmali)

# os modulu ıcındeki Path sınıfı 
# Genellikle dosyaların , klasorlerin uzantılarını degistirmede kullanilir

result = os.path.abspath("os.py")
print(result)
# dosyanin tam konumunu verir

result = os.path.dirname("dosyanin tam konumu yazilir(usttekini ciktisi)")
print(result)
# Tam konumu verilen dosyanin dizini cikti olarak alinir

result = os.path.dirname(os.path.abspath("os.oy"))
print(result)

result = os.path.exists("os.py")
# Aranilan konumda istedigim dosya var mi diye kontrol eder
print(result) # cikis  (True / False )
 
result = os.path.isdir(os.path.abspath("os.oy"))
# klasor mu degil mi diye kontrol eder
print(result) # cikis  (True / False )

result = os.path.isfile(os.path.abspath("os.oy"))
# dosya mı degil mi diye kontrol eder
print(result) # cikis  (True / False )

result = os.path.join("C:\\","deneme","deneme1")
# Parcalari birlestirir
print(result) # cikis  (True / False )

result = os.path.split("C:\\","deneme","deneme1")
# Parcalara ayirir
print(result) # cikis  (True / False )

result = os.path.splitext("os.py")
# Dosyanin ismiyle uzantisini degistirir
print(result) 

result = result[0]
print(result) 

result = result[1 ]
print(result) 
