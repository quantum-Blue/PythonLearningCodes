import pandas as pd
import numpy as np


# data
numbers = [1,2,3,4] # datatype int64
letters = ["a","s","d"] # 
letters = ["a","s","d",89] # datatype object
scalar=5
dict = {"a":10,"b":20,"c":30,"d":40}
random_numbers=np.random.randint(10,100,6)


# pandas_series = pd.Series() # bos array tanımlar
# pandas_series = pd.Series(numbers) # dizi tanımlar ancak index numaralını da yanında gosterir 
pandas_series = pd.Series(letters)
pandas_series = pd.Series(numbers)
pandas_series = pd.Series(scalar,[0,1,2,3]) # 0123 inex bilgisi
# pandas_series = pd.Series(numbers,[0,1,2]) # hata verir
pandas_series = pd.Series(numbers,[0,1,2,4]) # calisir
# pandas_series = pd.Series(numbers,[0,1,2,3,4]) # hata verir
pandas_series = pd.Series(dict) # harfler index sayısının yerine gecer
pandas_series = pd.Series(random_numbers)
pandas_series = pd.Series([20,30,40,50],["a","s","d","f"]) 
#  Harfler index numarası yerine geçer ama [0] yazarak da ilk elemana erisebiliriz

# print(pandas_series[0]) # ilk elemanı verır
# print(pandas_series[-1]) # sondan baslar
# print(pandas_series[:2]) # ilk 2 elemanı basar
# print(pandas_series[-2:]) # son 2 elemanı basar
# print(pandas_series["a"])
print(pandas_series.ndim) # kac boyutlu liste oldugunu soyler
print(pandas_series.dtype) # data turu
print(pandas_series.shape) # kaca kaclik liste oldugunu gosterir (4,1) 4 elemanli 1 boyutlu
print(pandas_series.sum)
print(pandas_series.max)
print(pandas_series.min)
print(pandas_series+pandas_series) # elemanları toplar

print(pandas_series) # default : dizini yazdırır ve turunu soyler

result = np.sqrt(pandas_series)
result = pandas_series % 2 == 0
result = pandas_series >= 15

print(result)

print(pandas_series[pandas_series % 2 == 0])

