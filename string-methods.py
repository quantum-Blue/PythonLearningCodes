message = ' Hello there. My name is Obi-Wan Kenobi'
print(message)
message = message.upper() # Her kelime buyuk harfli olur
print(message)
message = message.lower() # Her kelime kucuk harfli olur
print(message)
message = message.title() # Her kelimenin bas harfi buyuk olur
print(message)
message = message.capitalize() # Sadece ilk harf buyuk olur
print(message)
message = message.strip() # Bastaki ve sondaki bosluk karakterini siler
print(message)
message = message.lstrip() # Bastaki bosluk karakterini siler
print(message)
message = message.rstrip() # Sondaki bosluk karakterini siler
print(message)
message = message.split() # Her bir karakter bosluklardan ayrilarak kelime kelime yazdirilir
print(message)

message2 = ' Hello there. My name is Obi-Wan Kenobi'
message2 = message2.split('.') # .(nokta) karakterinden itibaren boler
print(message)
print(message[1])
message2=' '.join(message2) # Parca parca olan kelimeleri aralarina bosluk koyarak birlestirir

index = message2.find('Kenobi')
print(index) # Buldugu kelimenin ilk harfinin index numarasını dondurur
index = message2.rfind('Kenobi')
print(index) # Buldugu kelimenin ilk harfinin index numarasını dondurur ama SONDAN baslar
index = message2.find('Berserk')
print(index) # bulamazsa -1 degerini dondurur
isFound = message2.startswith('H') 
print(isFound) # Cumle H harfiyle basliyorsa True degerini dondurur
isFound2 = message2.endswith('i')
print(isFound2)
message2 = message2.replace('My' , 'His')
print(message2)
message2 = message2.replace(' ' , '-')
print(message2)
message2 = message2.replace(' ' , '-',5) # Sadece 5 kere yer degistirme islemi yapar
print(message2)
message2 = message2.replace(' ' , '') # Bosluklari siler
print(message2)

#Makalelerde bulunan turkce karakterleri düzeltmek icin kullanılabilir
"""
'''
# message = message.replace('ç','c').replace('ö','o')
# message = message.replace('ç','c')
#                  .replace('ö','o')
'''
"""

message2 = message2.center(100)
print(message2) # Cumleyi 100 karaktere tamamlar
message2 = message2.center(50,'*')
print(message2) # Saga ve sola esit karakter ekler, burda yildiz ekler
message2 = message2.ljust(50,'*')
print(message2) # Sola karakter ekler, burda yildiz ekler
message2 = message2.rjust(50,'*')
print(message2) # Saga karakter ekler, burda yildiz ekler
result2 = message2.count('a')
print(message2) # Kac tane a harfi gectigini gosterir
result2 = message2.count('bi')
print(message2) # Kac tane bi hecesinin gectigini gosterir
result2 = message2.count('e',0,12)
print(message2) # 0 dan 12 ye kadar kac tane e harfi gectigini gosterir
result2 = message2.index('e') # find method uyla aynı islevdedir (neredeyse)
print(message2)
result2 = message2.rindex('e') # rfind method uyla aynı islevdedir (neredeyse)
print(message2)
# find ve index arasindaki fark eger aranilan sozcuk bulunamazsa
# find methodunda -1 degeri dondurulur
# index methodunda ise hata mesaji ( exception ) verilir
result2 = message2.isalpha() # Cumlenin tamami HARFlerden mi olusmakta onu kontrol eder
result2 = message2.isdigit() # Cumlenin tamami SAYİlardan mi olusmakta onu kontrol eder
result2 = 'NAber'.isalpha()
result2 = '123'.isdigit()




