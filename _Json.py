# DOSYA ADİ KUTUPHANE ADİYLA AYNI OLAMAZ
import json

# dictionary hatırlatma
person = {"name":"Ali" , "languages":["c","c++"]}
result = person["name"]
print(result) 
result = person["languages"][1]
print(result) 
print("* "*10)

person_string = '{"name":"Ali" , "languages":["c","c++"]}'
# json dict in string icinde alınmıs hali

# Json String to Dict
result = json.loads(person_string)
print(type(result)) # <class 'dict'>
print(result)

# Dosyadaki Dict i Json a cevirdi
with open("person.json") as f:
    data = json.load(f)
    print(data)

# Dict to Json String
person_dict = {"name":"Ali" , "languages":["c","c++"]}
result = json.dumps(person_dict) 
print(type(result))
print(result)

# person_dict i person.json a yazar
with open("person.json","w") as f:
    json.dump(person_dict,f)
    
# person_string i dict yapip person_dict e esitler
person_dict = json.loads(person_string)

print(person_dict)
result = json.dumps(person_dict,indent=4,sort_keys=True)
# indent=4 : araya 4 bosluk koy
print(result)


