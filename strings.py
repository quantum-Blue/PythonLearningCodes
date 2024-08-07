name = 'Sadik'
surname = 'Turan'
age = 36
greeting ="My name is "+name+" and My surname is "+surname+".\nI am "+str(age)+" years old ."
length = len(greeting)
print(greeting)
print(greeting[0])
print(greeting[-1])
print(greeting[length-1])
print(greeting[0:7]) # 0 dan 7 ye kadar olanlari basar
print(greeting[0:]) # 0 dan en sona kadar olanlari basar
print(greeting[:13]) # 0 dan 13 kadar olanlari basar
print(greeting[:]) # 0 dan en sona kadar olanlari basar
print(greeting[::]) # 0 dan en sona kadar olanlari basar
print(greeting[4:40:2]) # 3 ten 40 a kadar olanları ikiser olarak basar

print("- - - - - - - - - - - - - - - - - - - -")

firstName = "Enes"
lastName = "Bal"
print("First Name : {} , Last Name : {}".format(firstName,lastName))
print("First Name : {0} , Last Name : {1}".format(firstName,lastName))
print("First Name : {1} , Last Name : {0}".format(firstName,lastName))
print("First Name : {f} , Last Name : {l}".format(f=firstName,l=lastName))
print("First Name : {l} , Last Name : {f}".format(f=firstName,l=lastName))
print("First Name : {} , Last Name : {} , My age is {}".format(firstName,lastName,'19'))
print("First Name : {f} , Last Name : {f}".format(f=firstName,l=lastName))
print("First Name : {} , Last Name : {}".format(firstName,firstName))
print(f"First Name : {firstName} , Last Name : {lastName}")

result = 21/7
print("The result is {}".format(result))
print(f"The result is {result}")
print("The result is {r}".format(r=result))
print("The result is {r:1.3}".format(r=result))
print("The result is {r:5.1}".format(r=result))

print("- - - - - - - - - - - - - - - - - - - - - ")

word = 'class'
print(word[::-1])   # class kelimesini tersten yazdirir

s = '123' * 5
print(s)

 


 