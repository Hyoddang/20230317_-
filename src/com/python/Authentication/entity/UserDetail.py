class UserDetail:

    def __init__(self,userId, phone, address, gender):
        self.userId = userId
        self.phone = phone
        self.address = address
        self.gender = gender

    def __str__(self):
        return f'[UserDetail]: userId= {self.userId}, phone= {self.phone}, address= {self.address}, gender= {self.gender}'