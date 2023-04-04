from src.com.python.Authentication.main.userListPage.UserListAll import UserListAll
from src.com.python.Authentication.main.userListPage.SearchUsers import SearchUsers

class UserList:

    @staticmethod
    def userList():
        while True:
            print("=====<< UserList >>=====")
            print("1. 전체 사용자 조회")
            print("2. 사용자 검색")
            print("b. 뒤로가기")
            print("====================")
            select = input("Menu Selected : ")
            if select == '1':
                UserListAll.userListAll()
            elif select == '2':
                SearchUsers.searchusers()
            elif select == 'b':
                break
            else:
                print("잘못 입력 하셨습니다.")
                print("====================")
                print()