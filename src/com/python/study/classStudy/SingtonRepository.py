class SingltonRepository:

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance == None:
            cls.instance = SingltonRepository()
        return cls.instance

    def __init__(self):
        self.userList = list()
















