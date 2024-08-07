
import random

for i in range(5):
    print("{:.4f}".format(random.random()))
'''
Bu kod, Python programlama dilinde rastgele on adet ondalık sayı oluşturur ve bu sayıları ekrana 4 ondalık basamakla yazdırır. 
Kod, Python'da rastgele sayılar oluşturmak için yerleşik olan `random` modülünü kullanır.

1. `import random`: Bu satır, `random` modülünü programa dahil eder,
böylece rastgele sayıları oluşturmak için bu modülü kullanabiliriz.

2. `for i in range(10):`: Bu döngü 0'dan 9'a kadar (10 dahil değil) olan sayıları temsil eden `i` değişkenini oluşturur.
Yani bu döngü 10 kez çalışacak.

3. `random.random()`: Bu ifade, 0 ile 1 arasında rastgele bir ondalık sayı üretir.

4. `"{:.4f}".format(random.random())`: Bu ifade, `random.random()` ile oluşturulan rastgele sayıyı 4 ondalık basamakla biçimlendirir.

5. `print("{:.4f}".format(random.random()))`: Bu ifade, biçimlendirilmiş rastgele sayıları ekrana yazdırır.

Bu kodu çalıştırdığınızda, her çalıştırıldığında farklı ondalık sayılar elde edeceksiniz.
'''
print(random.randint(45, 500))
# randint 45 ve 500 arasindan raastgele bir int sayi dondurur
liste = ['ali', 'veli', 'ahmet', 'mehmet', 'celal', 'selin', 'nihat']
print(random.choice(liste))
# choice dizi lerden rastgele bir elemani basar

# Rastgele sayiyi bulma oyunu
can = int(input("kac caniniz olsun: "))
sayac = can
answer = random.randint(1,30)
sayi = 0
print(f"{sayac} hakkiniz var rastgele 1 ile 30 arasindaki sayiyi bulun")
while(sayac > 0):
    sayi = int(input("sayi girin: "))
    sayac-=1
    if sayi == answer:    
        print(f"Tebrikler sayiyi {sayac} denemede buldunuz. Sayinin degeri : {answer}")
        print(f"Puaniniz : {100-(sayac*(100/can))}")
        break
    elif sayi > answer:
        print("Daha kucuk bir sayi girin.")
    elif sayi < answer:
        print("Daha buyuk bir sayi girin.")
else:
    print("Sayiyi bulamadiniz. Sayinin degeri : " ,answer)
    print(f"Puaniniz: {100-((100/can)*(sayac-1))}")

# Chat-GPT versiyonu
"""
import random

sayac = 0
hak = 5
answer = random.randint(1, 30)

print("5 hakkiniz var, rastgele 1 ile 30 arasindaki sayiyi bulun")

while sayac < hak:
    try:
        sayi = int(input("Tahmininizi girin: "))
        sayac += 1
        if sayi == answer:
            print("Tebrikler, sayiyi buldunuz. Sayinin degeri:", answer)
            break
        elif sayi > answer:
            print("Daha kucuk bir sayi girin.")
        elif sayi < answer:
            print("Daha buyuk bir sayi girin.")
        print("Kalan hak: ", hak - sayac)
    except ValueError:
        print("Lutfen gecerli bir sayi girin.")

else:
    print("Sayiyi bulamadiniz. Dogru sayi:", answer)

"""

# Alttaki BlackBox un baska garip bi ornegi
"""
from transformers import pipeline

# Chatbot için gerekli pipeline'ı oluşturuyoruz
chatbot_pipeline = pipeline("conversational")

chat_history = ["Merhaba"]

def greeting():
    responses = ["Naberim?", "Orada mısın?", "Selam", "Selamun aleykum"]
    return responses

def question(msg):
    return f"{msg}?"

def conversation(msg):
    global chat_history
    if msg.lower() == "hi":
        responses = greeting()
        chat_history.extend(responses)  # Yanıtları chat geçmişine ekler
    elif msg.lower() == 'bye':
        return "Hoşça kal! Görüşmek üzere."
    else:
        return question(msg)

# Chatbot ile etkileşim
while True:
    kullanici_girdisi = input("Siz: ")
    chat_response = conversation(kullanici_girdisi)
    chat_history.append(kullanici_girdisi)
    chat_history.append(chat_response)
    print("Chatbot: ", chat_response)

    # İstediğiniz bir koşula göre döngüyü sonlandırabilirsiniz, örneğin kullanıcı 'bye' dediğinde.
    if kullanici_girdisi.lower() == 'bye':
        break
"""
# aciklamasi soyle
"""
Bu kod, kullanıcıdan gelen girdileri dinleyen bir chatbot oluşturur. Kullanıcı 'hi' dediğinde bot selamlaşıyor, 'bye' dediğinde hoşça kal diyor ve sohbeti bitiriyor. Diğer durumlarda kullanıcıya verilen girdiyi bir soru olarak yanıtlıyor.
Kodun tam olarak ihtiyacınıza uygun hale getirilmesi için istediğiniz gibi özelleştirebilirsiniz. Bu örnek, kullanıcıdan gelen girdileri dinleyen basit bir chatbot yapısını temsil etmektedir.
"""

# Sayinin asal olup olmadigini bulan kod
sayi = int(input("Sayi girin: "))
i = 2
asalMi = True
if sayi < 2:
    asalMi = False
for i in range(2,sayi):
    if sayi%i==0:
        asalMi=False
        break
if asalMi:
    print("sayi asal")
else:
    print("sayi asal degildir.")




