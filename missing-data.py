import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])



result = df

# axis = 1 ise sütun(kolon) , axis = 0 ise satır
result = df.drop("column1",axis=1)
result = df.drop("a",axis=0)
result = df.drop(["a","b","c"],axis=0)
result = df.isnull() # Nan (not a number)
result = df.notnull()
result = df.isnull().sum()
result = df["column1"].isnull().sum()


print(result)


newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

print(df)

result = df[df["column1"].isnull()] # bos satirlari goruntuler
result = df[df["column1"].isnull()]["column1"] # column1 deki bos satirlari goruntuler
result = df[df["column1"].notnull()]["column1"]
result = df.dropna() # bos satirlari siler / varsayılan axis = 0 (satıra gore)
result = df.dropna(axis=1) # bos sütunlari siler
result = df.dropna(how="any") # herhangi bir Nan deger bulursa siler 
result = df.dropna(how="all") 
# oldugu gibi Nan olan satırlar filtreleme içinden çıkarılır
# tüm satır Nan ise karşımıza gelmez 
result = df.dropna(subset=["column1","column2"],how="all")
# tüm sütun Nan ise karşımıza gelmez 
result = df.dropna(subset=["column1","column2"],how="any")
result = df.dropna(thresh=2) # 2 tane normal veri varsa silme işlemi yapmaz!
result = df.dropna(thresh=3) # en az sayida normal veri
result = df.fillna(value="no input") # Nan degerlerine no input yazar
result = df.fillna(value=1)
result = df.sum().sum()
result = df.isnull().sum()
result = df.isnull().sum().sum()


print(result)




def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet 

result = df.fillna(value=ortalama(df)) # tum not olan yerlere ortalama yazılır
print(result)



