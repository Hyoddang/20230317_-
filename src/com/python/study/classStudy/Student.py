class Student:
    def __init__(self, name, age):                             # 자료구조, 알고리즘
        self.name = name                                       # classStudy = 자료형
        self.age = age

    def showInfo(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')

    @classmethod
    def classMethod(cls, _name):
        cls._name = _name

    @classmethod
    def classMethod2(cls):
        print(cls._name)


    @staticmethod
    def staticMethod():
        print('static test')


































