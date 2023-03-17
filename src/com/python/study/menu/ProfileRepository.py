class ProfileRepository:

    userList = list()

    @classmethod
    def insertUser(cls, userEntity):
        cls.userList.append(userEntity)

    @classmethod
    def selectAllUser(cls):
        return cls.userList
