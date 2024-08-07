# YONTEM 1
'''
import math

value = dir(math)
print(value)

value = help(math)
print(value)

value = help(math.factorial)
print(value)

value = math.sqrt(25)
print(value)

value = math.floor(2.8)
print(value)

value = math.ceil(2.5)
print(value)

value = math.factorial(5)
print(value)


import math as islem
value = islem.factorial(4)
'''

# YONTEM 2

# from math import * # math kutuphanesi icindeki tum metodlari import eder
from math import factorial,sqrt # sadece factorial ve sqrt metodunu import eder

value = factorial(5)
print(value)

value = sqrt(25)
print(value)

# value = ceil(4.6) # hata verir
