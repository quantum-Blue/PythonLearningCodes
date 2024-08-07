import numpy as np

# python list
py_list=[1,2,3,4,5,6]

# numpay array
np_array = np.array([1,2,3,4,5,6])

print("Python List: ", type(py_list))
print("NP Array: ", type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)

print(py_multi)
print(np_multi)

print(np_array.ndim)
print(np_multi.ndim)

print(np_array.shape)
print(np_multi.shape)

result = np.arange(1,10)
print(result) # 1 den 9 a kadar olan sayıları array halinde gösterir

result = np.arange(1,10,2)
print(result) # 1 den 9 a kadar olan sayıları  2 şer arttırarak array halinde gösterir

result = np.zeros(10)
print(result) # 10 tane 0 dan olusan dizi olusturur

result = np.ones(10)
print(result) # 10 tane 1 dan olusan dizi olusturur

result = np.linspace(1,100,5)
print(result) # 1 den 100 e kadar olan sayıları 5 parcaya boler ve bolunen yerleri gosterir


 
"""
1 ile 10 arasında 100 kere deneme yaparak 10 sayisinin gelme olasiigini hesaplayan kodu yaz !!!!
"""


result = np.random.randint(0,10)
print(result) # 0 - 10 arasinda sayi gosterir (0 dahil, 10 dahil degil)

result = np.random.randint(0,10,2)
print(result) # 0 - 10 arasinda 2 tane sayi gosterir (0 dahil, 10 dahil degil)

result = np.random.rand(5)
print(result) # 0 - 5 arasinda double sayi gosterir (0 dahil, 10 dahil degil)

result = np.random.randn(5)
print(result) # 0 - 5 arasinda double arti ve eksi sayilari gosterir (0 dahil, 10 dahil degil)

np_array = np.arange(50)
result = np_array.reshape(5,10)
print(result) #  5 e 10luk matrise cevirir

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis=1)) # satirlarin toplamini verir

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis=1)) # sutunlarin toplamini verir

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()
print(result)
result = rnd_numbers.min()
print(result)
result = rnd_numbers.mean() # uretilen sayilarin ortalamasi
print(result)
result = rnd_numbers.argmax() # uretilen max sayinin index numarasi
print(result)
result = rnd_numbers.argmax() # uretilen min sayinin index numarasi
print(result)

numbers = np.array([1,2,3,4,524,4325,3253,2])
result = numbers[5]
print(result)
result = numbers[-1]
print(result)
result = numbers[0:3]
print(result)
result = numbers[:3]
print(result)
result = numbers[3:]
print(result)
result = numbers[::]
print(result)
result = numbers[::-1]
print(result)
result = numbers[::-2]
print(result)

numbers2 = np.array([[1,2,3,],[12,23,34],[34,6,8]])
print(numbers2)
result = numbers2[1]
print(result)
result = numbers2[2,0]
print(result)
result = numbers2[:,2] # tum satirlarin ikinci degerlerini yazdirir
print(result)
result = numbers2[-1,:] # sondakinin tum degerlerini yazdirir
print(result)
result = numbers2[:2,:2] # wakarani
print(result)
 
arr1 = np.arange(0,10)
#arr2 = arr1 # referans
arr2 = arr1.copy()

print(arr1)
print(arr2)

arr2[0] = 20

print(arr1)
print(arr2)

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
numbers3 = numbers1 + numbers2 
print(numbers3)
numbers3 = numbers1 + numbers2 
print(numbers3)
numbers3 = numbers1 - numbers2 
print(numbers3)
numbers3 = numbers1 + 10 
print(numbers3)
numbers3 = numbers1 - 10
print(numbers3)
numbers3 = numbers1 * 10
print(numbers3)
numbers3 = numbers1 * numbers2 # aynı index deki elemanlar carpilir
print(numbers3)
numbers3 = numbers1 / 10
print(numbers3)
numbers3 = numbers1 / numbers2 
print(numbers3)

result = np.sin(numbers1) 
print(result)
result = np.cos(numbers1) 
print(result)
result = np.sqrt(numbers1) 
print(result)
result = np.log(numbers1) 
print(result)

numbers1 = numbers1.reshape(2,3)
numbers2 = numbers2.reshape(2,3)
print(numbers1)
print(numbers2)

result = np.vstack(numbers1,numbers2)
print(result) # dikey birlestirme islemi yapar ()
result = np.hstack(numbers1,numbers2)
print(result) # yatay birlestirme islemi yapar (horizontal)

result = numbers1 >= 5
print(result)
result = numbers1 % 2 == 5
print(numbers1[result])
print(result)


