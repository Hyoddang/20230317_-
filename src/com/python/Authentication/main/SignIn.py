from src.com.python.Authentication.repository.UserRepository import UserRepository
from src.com.python.Authentication.security.PrincipalUser import PrincipalUser
class SignIn:
    @staticmethod
    def signIn():
        print("=====<< 로그인 >>=====")
        username = None
        password = None

        while True:
            username = input('username : ')
            if len(username) > 0:
                break
            else:
                print("사용자이름을 입력 해주세요.")

        while True:
            password = input('password : ')
            if len(password) > 0:
                break
            else:
                print("비밀번호를 입력 해주세요.")

        userDict = UserRepository.findUserByUsername(username)
        if userDict == None:
            return False

        if userDict.get('password') == password:
            PrincipalUser.setSession(userDict)
            return True
        else:
            return False