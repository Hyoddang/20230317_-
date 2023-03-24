class User:

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __str__(self):
        return f'[User]: username= {self.username}, password= {self.password}, name= {self.name}, email= {self.email}'
