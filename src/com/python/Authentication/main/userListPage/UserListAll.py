from src.com.python.Authentication.repository.UserRepository import UserRepository

class UserListAll:

    @staticmethod
    def userListAll():
        usersDictList = UserRepository.getUsers()
        print(f'{"ID":<8s}{"사용자이름":<8s}{"성명":<8s}{"이메일":<20s}{"연락처":<16s}{"주소":<20s}성별')


if __name__ == "__main__":
    UserListAll.userListAll()