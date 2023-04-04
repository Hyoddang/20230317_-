from src.com.python.Authentication.repository.UserRepository import UserRepository

class UserListAll:

    @staticmethod
    def userListAll():
        usersDictList = UserRepository.getUsers()
        print(f'{"ID":<8s}{"사용자이름":<8s}{"성명":<8s}{"이메일":<20s}{"연락처":<16s}{"주소":<20s}성별')
        for userDict in usersDictList:
            print(userDict)
            print(f'{userDict.get("user_id"):<8d}{userDict.get("username"):<8s}{userDict.get("name"):<8s}{userDict.get("email"):<20s}{str(userDict.get("phone")):<16s}{str(userDict.get("address")):<20s}{str(userDict.get("gender"))}')
    # def userListAll():
    #     usersDictList = UserRepository.getUsers()
    #     print(f'{"ID":<8s}{"사용자 이름":<12s}{"성명":<8s}{"이메일":<30s}{"연락처":<16s}{"주소":<40s}{"성별"}')
    #     for userDict in usersDictList:
    #         print(
    #             f'{userDict.get("user_id"):<8d}{userDict.get("username"):<12s}{userDict.get("name"):<8s}{userDict.get("email"):<30s}{str(userDict.get("phone")):<16s}{str(userDict.get("address")):<40s}{str(userDict.get("gender"))}')


if __name__ == "__main__":
    UserListAll.userListAll()