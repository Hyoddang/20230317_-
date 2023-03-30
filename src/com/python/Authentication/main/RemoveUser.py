from src.com.python.Authentication.config.GlobalConfig import GlobalConfig
from src.com.python.Authentication.security.PrincipalUser import PrincipalUser
from src.com.python.Authentication.repository.UserRepository import UserRepository


class RemoveUser:

    @staticmethod
    def removeUser():
        select = input("회원 탈퇴에 동의 하십니까? 계속 하려면 (Y/y) 입력, 취소 하려면 아무키나 입력 : ")
        if select != 'Y' and select != 'y':
            return

        UserRepository.removeUserByUsername(PrincipalUser.session.get('username'))
        PrincipalUser.clearSession()
        print('회원 탈퇴 완료.')
        GlobalConfig.stopLoop()