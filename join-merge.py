import pandas as pd

customers = {
    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]
}

orders = {
    "OrderId":[10,11,12,13],
    "CustomerId":[1,2,5,7],
    "OrderDate":["2010-07-04","2010-08-04","2010-07-07","2012-07-04"]
}

df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers,df_orders,how="inner") # inner joinle ortak sutunu birlestirir
print(result)

result = pd.merge(df_customers,df_orders,how="left") # left joinle ortak sutunu birlestirir
print(result)

result = pd.merge(df_customers,df_orders,how="right") # right joinle ortak sutunu birlestirir
print(result)

result = pd.merge(df_customers,df_orders,how="outer") # outer joinle ortak sutunu birlestirir
print(result)



customerA = {
    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]
}

customerB = {
    "CustomerId":[4,5,6,7],
    "FirstName":["Yagmur","Cinar","Cengiz","Can"],
    "LastName":["Bilge","Turan","Yilmaz","Turan"]
}

df_customerA = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_customerB = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])

result = pd.concat(df_customerA,df_customerB) # default axis = 1 (degistirilebilir)

print(result)





