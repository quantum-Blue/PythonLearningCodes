
import random

result = dir(random)
result = help(random)
print(result)

result = random.random() # 0.0 ile 1.0 arasinda sayi uretir
print(result)
result = random.random() * 100
print(result)
result = int(random.uniform(10,100)) # 10 ile 100 arasinda sayi uretir
print(result)
result = random.randint(1,100)
print(result)

names = ['ali','yagmur','deniz','cenk','cenk']
result = names[random.randint(0,len(names)-1)]
print(result)
result = random.choice(names)
print(result)
result = random.sample(names,3)
print(result)

greeting = 'Hello There'
result = random.choice(greeting)
print(result)

liste = list(range(10))
random.shuffle(liste)
result = liste
print(result)
#karisik bir sekilde 1 den 10 a kadar olan sayilari siralar

liste = range(100)
result = random.sample(liste,3)
# 100 e kadar olan sayilarin icinden rastgele 3 tanesini basar
print(result)

