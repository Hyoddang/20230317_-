from src.com.python.Authentication.config.GlobalConfig import GlobalConfig
from src.com.python.Authentication.security.PrincipalUser import PrincipalUser
from src.com.python.Authentication.main.ModifyUser import ModifyUser
from src.com.python.Authentication.main.RemoveUser import RemoveUser



class MyPage:

    @staticmethod
    def myPage():
        flagIndex = GlobalConfig.addLoopFlagList()
        while GlobalConfig.loopFlagList[flagIndex]:
            print("=====<< MyPage >>=====")
            print(f"사용자이름 : {PrincipalUser.session.get('username')}")
            print(f"성명 : {PrincipalUser.session.get('name')}")
            print(f"이메일 : {PrincipalUser.session.get('email')}")
            print(f"연락처 : {PrincipalUser.session.get('phone')}")
            print(f"주소 : {PrincipalUser.session.get('address')}")
            print(f"성별 : {PrincipalUser.session.get('gender')}")
            print("====================")
            print("1. 회원정보 수정")
            print("2. 회원 탈퇴")
            print("b. 뒤로가기")
            print("====================")
            select = input("Menu Selected : ")
            if select == 'b':
                break
            elif select == '1':
                ModifyUser.modifyUser()
            elif select == '2':
                RemoveUser.removeUser()
            else:
                print("잘못 입력 하셨습니다.")
                print("====================")
                print()