'''
Tenemos que desarrollar un sistema para validar el login con diferentes usuarios.

La informacion de usuario se encuentra en un JSON.
[
    {"email": "usuario1@qaminds.com", "password": "adsfsdfsd"},
    {"email": "usuario4@qaminds.com", "password": "dfsaf"},
    {"email": "fdasfdsadf", "password": "dsfs"}
]


El sistema que modelar cada usuario con una clase.
'''


import json


class User:
    def __init__(self, email: str, password: str):
        self.__email = email
        self.__password = password

    def login(self):
        # REST API para emular el login
        # Selenium Code para hacer login en pagina
        print(f"Login utilizando usuario: {self}")

    def logout(self):
        print(f"Logout utilizando usuario: {self}")

    def remove(self):
        pass

    def update(self):
        pass

    def __str__(self):
        return f"(email={self.__email}, password={self.__password})"

    def __repr__(self):
        return f"(email={self.__email}, password={self.__password})"


def load_users(file_name: str) -> list:
    users = []
    with open(file_name) as file:
        raw_users = json.load(file)
        for raw_user in raw_users:
            user = User(**raw_user)
            users.append(user)
    return users


def test_user_login(user: User):
    print("-" * 80)
    print(f"Realizar prueba de login para usuario: {user}")
    print("Abrir navegador")
    user.login()
    print("Validar que estoy en la pagina de login")


def test_user_logout(user: User):
    print("-" * 80)
    print(f"Realizar prueba de logout para usuario: {user}")
    print("Abrir navegador")
    user.logout()
    print("Validar que estoy en la pagina de iniciar session")


users = load_users("users.json")
for user in users:
    test_user_login(user)
    test_user_logout(user)


for index in range(10000):
    user = User("luis@qaminds.com", "password123")
    test_user_login(user)
    test_user_logout(user)