from src.com.python.Authentication.config.GlobalConfig import GlobalConfig
from src.com.python.Authentication.security.PrincipalUser import PrincipalUser
from src.com.python.Authentication.main.MyPage import MyPage
from src.com.python.Authentication.main.userListPage.UserList import UserList

class Home:

    @staticmethod
    def home():
        flagIndex = GlobalConfig.addLoopFlagList()
        while GlobalConfig.loopFlagList[flagIndex]:
            print("=====<< Home >>=====")
            print(f"접속한 사용자이름 : {PrincipalUser.session.get('username')}")
            print("====================")
            print("1. 마이 페이지")
            print("2. 사용자정보 조회")
            print("3. 로그아웃")
            print("====================")
            select = input("Menu Selected : ")
            if select == '1':
                MyPage.myPage()
            elif select == '2':
                UserList.userList()
            elif select == '3':
                PrincipalUser.clearSession()
                break
            else:
                print("잘못 입력 하셨습니다.")
                print("====================")
                print()