import matplotlib.pyplot as plt
import numpy as np

# Ornek - 1
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r")
plt.axis([0,6,0,20])

plt.title("Grafik Basligi")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()
"""

# Ornek - 2
"""
x = np.linspace(0,2,100)

plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3,label="Cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Simple Plot")
plt.legend()

plt.show()
"""


# Stack Plot
"""
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]

plt.plot([],[],label="oyuncu1",color="y")
plt.plot([],[],label="oyuncu2",color="r")
plt.plot([],[],label="oyuncu3",color="b")


plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])


plt.xlabel("Yil")
plt.ylabel("Gol Sayisi")
plt.title("Yillara Gore Atilan Goller")
plt.legend()

plt.show()

"""

# Pie Grafigi
"""
goal_types = "Penalti" , "Kaleye Atilan Sut" , "süSerbest Vurus"

goals = [12,35,7]
colors = ["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05))

plt.show()
"""


# Bar Grafigi
"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Gun")
plt.ylabel("Mesafe (Km)")
plt.title("Arac Bilgiler")

plt.show()
"""

# Histogram Grafigi

yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("Yas Gruplari")
plt.ylabel("Kisi Sayisi")
plt.title("Histogram Grafigi")

plt.show()
