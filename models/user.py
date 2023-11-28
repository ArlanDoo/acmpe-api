import datetime

class User:
    def __init__(self, _id: str, first_name: str, last_name: str,
                 birthday: str, age: int, email: str, city: str):
        self.id = _id
        self.firstname = first_name
        self.lastname = last_name
        self.birthday = birthday
        self.age = age
        self.email = email
        self.city = city