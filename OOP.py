# Object Oriented Programming (OOP)
# class
# instance (object)
class Empty:
    pass
# hic bir sey yapmayan class
e1 = Empty()
print(e1)
#adresi yazar
e2 = Empty()
print(e2)

print(type(e1))
print(type(e2))
print(e1 == e2)

# class
class Person:
    # class attributes
    adress = 'no information'
    # constructor (yapici method)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print("init methodu calisti")
        
    # instance methods
    def intro(self):
        print(f"Hello There, I am {self.name}")

    def calculateAge(self):
        return 2023 - self.year


# object instance        
p1 = Person('ali', 1990)
p2 = Person('yagmur', 1995)

p1.intro()
p2.intro()

print(f"My age: {p1.calculateAge}")
print(f"My age: {p2.calculateAge}")

# updating
p1.name = 'ahmet'
p1.adress = 'kocaeli'

# accesing object attributes
print(f"p1; name: {p1.name}, year: {p1.year}, adress: {p1.adress}")
print(f"p2; name: {p2.name}, year: {p2.year}, adress: {p2.adress}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))

print("* "*20)

class Circle:
    # class attribute
    # def __init__(self) -> None:
    #     pass
    pi = 3.14

    def __init__(self,yariCap=1):
        self.yariCap = yariCap
    # methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yariCap
    def alanHesapla(self):
        return self.pi * (self.yariCap ** 2)
    
c1 = Circle() # r = 1
c2 = Circle(5)

print(f"c1; alan: {c1.alanHesapla()}, cevre: {c1.cevreHesapla()}")
print(f"c2; alan: {c2.alanHesapla()}, cevre: {c2.cevreHesapla()}")

print("* "*20)

# inheritance (kalitim)

class Person():
    def __init__(self):
        print("Person Created")
class Student(Person):
    pass

p1 = Person()
s1 = Student()

class Person():

    def __init__(self, fname, lname):
        print("Person Created")
        self.firstname=fname
        self.lastname=lname

    def who_am_i(self):
        print('I am a Person')

    def eat(self):
        print("I am eating")

class Student(Person):

    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print("Student Created")

    # Override    
    def who_am_i(self):
        print("I am a Student")

    def sayHello(self):
        print("Hello I'm a student")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname) # super methodu !! self gondermeye gerek yok , personu tanimliyor
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} Teacher")
    #del who_am_i()
p1 = Person('Ali', 'Yilmaz')
s1 = Student('Cinar', 'Turan', 3469)
t1 = Teacher('Serkan', 'Yilmaz', 'Math')

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()



