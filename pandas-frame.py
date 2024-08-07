import pandas as pd
import numpy.random as randn


s1=pd.Series([3,2,0,1])
s2=pd.Series([0,3,7,2])

data=dict(apples=s1 , oranges=s2)
df=pd.DataFrame(data)
print("Dataframe: \n", df)


data= [["Enes",100],["Ahmet",50],["Mehmet",45],["Ali",30]]
df=pd.DataFrame(data,columns=["Names","Grades"],index=[1,2,3,4],dtype=float)
print(df) # satır ve sutun numaraları var


list = [["Asli",12],["Ali",23],["Can",41],["Mert",67]]
dict = {"Name":["Asli","Ali","Can","Mert"],"Grade":[12,23,41,67]}
dict_list = [
    {"Name": "Asli","Grade":12},
    {"Name":"Ali","Grade": 23},
    {"Name":"Can","Grade": 41},
    {"Name":"Mert","Grade": 67}
]

df=pd.DataFrame(dict_list,index=[212,232,236,456])
print(df)

# Video - 20.4 ss i var

df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
result=df
result=df["Column1"]
result=type(df["Column1"])
result=df[["Column1","Column2"]]
# loc["row","column"] => loc["row"] => loc[":","column"]
result=df.loc["A"] # loc : location / indexi A olan elemanları dizi halinde gosterir
result=type(df.loc["A"])
result=df.iloc[2]
result=df.loc[:,"Column1"]
result=df.loc[:,["Column1","Column2"]]
result=df.loc[:,"Column1":"Column2"]
result=df.loc[:,:"Column2"]
result=df.loc["A":"B",:"Column2"]
result=df.loc[:"B",:"Column2"]

print(result)

df["Column4"]=pd.Series(randn(3),["A","B","C"]) # yukaridan asagi dizi olusturup dataframe ekledik
print(df)

result=df["Column5"]=df["Column1"]+df["Column3"]
print(df.drop("Column5",axis=1,inplace=True))
print(result)
print(df)

