import re
# regular expression

result = dir(re)
print("Result:", result)

str = "Python Kursu : Python Programlama"

result = re.findall("Python",str)
# Python kelimelerşni bulur ve listeler
print(result)

result = len(result)
print(result)

result = re.split(" ",str)
print(result)

result = re.sub(" ","-")
# Bosluk karakterlerini - ile degistirir
print(result)

result = re.split("%s","-")
# Usttekiyle aynı
print(result)

result = result.span()
print(result)

result = result.start()
print(result)

result = result.end()
print(result)

result = result.group()
print(result)

result = result.string
print(result)


result = re.findall("[abc]",str)
# a b ve c karakterlerini str de arar ve gosterir liste halinde
print(result)

result = re.findall("[a-e]",str)
# a dan e ye kadar olan karakterlerini str de arar ve gosterir liste halinde
print(result)

"""
[1-10]
1 den 10 a kadar olan
[^abc]
abc olmayan
[a-zA-Z0-9_]
harf, rakam ve altcizgiyi iceren
[...]
3 lu gruplar
[Py..on]
[Pyt?on]
[al{2}]
a karakteri 1 l karakteri 2 kere tekrarlanmali
[al{2,3}]
a karakteri 1 l karakteri 2 veya 3 kere tekrarlanmali
[0-9{2,4}]
2 ila 4 karekterden (basamaktan) olusur
{(a|b|c)xz}
a,b,c den biri ve arkasından xz
"""

# Cok fazla şey var kalanına internetten bak Python RegEx


