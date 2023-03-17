from src.com.python.study.menu.MenuView import MenuView
from src.com.python.study.menu.CommonMessage import CommonMessage
from src.com.python.study.menu.ProfileService import ProfileService

class MainMenuController:

    @staticmethod
    def showSelectProfileMenu():
        while True:
            print(MenuView.getSelectProfileMenu())
            print(MenuView.getBackMenu())
            selected = input('메뉴 번호를 입력하세요.: ')
            if selected == 'b':
                break
            elif selected == '1':
                ProfileService.showUserAll()
            elif selected == '2':
                pass
            else:
                print(CommonMessage.getselectedMenuErrorMessage())
            print()

    @staticmethod
    def showAddProfileMenu():
        while True:
            print(MenuView.getAddProfileMenu())
            print(MenuView.getBackMenu())
            selected = input('메뉴 번호를 입력하세요.: ')
            if selected == 'b':
                break
            elif selected == '1':
                ProfileService.addUser()
            else:
                print(CommonMessage.getselectedMenuErrorMessage())
            print()
