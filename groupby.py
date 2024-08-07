import pandas as pd
import numpy as np


personeller = {
    "Calisan":["Ahmet Yilmaz","Can Erturk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Riza Erturk","Mustafa Can"],
    "Departman":["Insan Kaynaklari","Bilgi Islem","Muhasebe","Insan Kaynaklari","Bilgi Islem","Muhasebe","Insan Kaynaklari"],
    "Yas":[30,25,45,50,23,34,42],
    "Semt":["Kadikoy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadikoy"],
    "Maas":[5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)
result=df
result=df["Maas"].sum()
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups
semtler=df.groupby("Semt")

for name,group in df.groupby("Departman"):
    print(name)
    print(group)

for name,group in df.groupby("Semt"):
    print(name)
    print(group)

result = df.groupby("Semtler").get_group("Kadikoy")
result = df.groupby("Departman").get_group("Muhasebe")
result = df.groupby("Departman").sum()
result = df.groupby("Departman").mean()
result = df.groupby("Semt")["Yas"].mean()
result = df.groupby("Semt")["Maas"].mean()
result = df.groupby("Semt")["Calisan"].count() # semtlere gore calisan sayisi
result = df.groupby("Departman")["Yas"].max() 
result = df.groupby("Departman")["Maas"].min()
result = df.groupby("Departman")["Maas"].max()["Muhasebe"]  
result = df.groupby("Departman").agg(np.mean) # departmana gore ortalama hesaplama
result = df.groupby("Departman")["Maas"].agg(np.sum,np.mean,np.max,np.min).loc["Muhasebe"] 


print(result)

