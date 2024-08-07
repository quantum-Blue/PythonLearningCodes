
import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
# repository : depo
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.LoadUsers()

    def LoadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    print(user["username"])
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanici olusturuldu.")

    def login(self,username,password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login yapildi")
                break
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}

        print("Cikis yapildi.")
    
    def identity(self):
        if self.isLoggedIn == True:
            print(f"username: {self.currentUser.username}")
        else:
            print("Giris yapilmadi.")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open("users.json","w") as file:
            json.dump(list,file)

repository = UserRepository()

while True:

    print("Menu".center(50,"*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeciminiz: ")

    if secim == "5":
        break

    else:
        if secim == "1":
        # register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            user = User(username=username,password=password,email=email)
            repository.register(user)

        elif secim == "2":
            # login
            if repository.isLoggedIn:
                print("Zaten Login oldunuz.")
            else:
                username = input("username: ")
                password = input("password: ")   
                repository.login(username,password)

        elif secim == "3":
            # logout
            repository.logout()

        elif secim == "4":
            # identity : kimlik
            # display username : kullanıcı adını goster
            repository.identity()


            


'''import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.LoadUsers()

    def LoadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                for user_data in data:
                    newUser = User(username=user_data["username"], password=user_data["password"], email=user_data["email"])
                    self.users.append(newUser)
                print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login yapıldı")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı.")

    def identity(self):
        if self.isLoggedIn:
            print(f"Kullanıcı Adı: {self.currentUser.username}")
        else:
            print("Giriş yapılmadı.")

    def savetoFile(self):
        user_data_list = [json.dumps(user.__dict__) for user in self.users]
        with open("users.json", "w") as file:
            json.dump(user_data_list, file)

repository = UserRepository()

while True:
    print("Menu".center(50, "*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz: ")

    if secim == "5":
        break
    else:
        if secim == "1":
            # register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == "2":
            # login
            if repository.isLoggedIn:
                print("Zaten Login oldunuz.")
            else:
                username = input("username: ")
                password = input("password: ")
                repository.login(username, password)

        elif secim == "3":
            # logout
            repository.logout()

        elif secim == "4":
            # identity
            repository.identity()
'''