import pandas as pd
import numpy as np

data = {
    "column1":[1,2,3,4,5],
    "column2":[10,20,13,45,25],
    "column3":["abc","bca","ade","cba","dea"]
}

df = pd.DataFrame(data)

result = df
result = df["column2"].unique() # tekrarlanmayan bilgileri basar
result = df["column2"].nunique() # tekrarkanmayan bilgilerin sayısını basar
result = df["column2"].value_counts() # her sayıdan kaç tane oldugunu gosterir
result = df["column1"]*2

print(result)

def kareal(x):
    return x**2

result = df["column1"].apply(kareal) # column1 deki degerler sırasıyla kareal fonx una gonderilirler

kareal2 = lambda x : x**2
result = df["column1"].apply(kareal2)

result = df["column1"].apply(lambda x:x**2) # usttekinin otomatik fonx olusturulmus hali
print(result)

result = df["column3"].apply(len) # column3 deki eleman sayısı
print(result)

df["column4"] = df["column3"].apply(len)
print(df)

result = df.columns
print(result)

result = len(df.columns)
print(result)

result = df.index
print(result) # ilk ve son indexi ve artıs miktarini verir

result = df.sort_values("column1")
print(result)

result = df.sort_values("column2")
print(result)

result = df.sort_values("column3",ascending=True) # tersten sıralar
print(result)


data = {
    "Ay":["Mayis","Haziran","Nisan","Mayis","Haziran","Nisan","Mayis","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir":[20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

df = pd.pivot_table(index="Ay",columns="Kategori",values="Gelir")

print(df)

