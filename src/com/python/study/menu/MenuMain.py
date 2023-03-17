from src.com.python.study.menu.MenuView import MenuView
from src.com.python.study.menu.CommonMessage import CommonMessage
from src.com.python.study.menu.MainMenuController import MainMenuController
if __name__ == '__main__':

    print('메뉴 프로그램')
    while True:
        print(MenuView.getMainMenu())
        print(MenuView.getExitMenu())
        selected = input('메뉴 번호를 입력하세요.: ')
        if selected == 'q':
            print('시스템이 종료 되었습니다.')
            break
        elif selected == '1':
            MainMenuController.showSelectProfileMenu()
        elif selected == '2':
            MainMenuController.showAddProfileMenu()
        elif selected == '3':
            pass
        elif selected == '4':
            pass
        else:
            print(CommonMessage.getselectedMenuErrorMessage())
        print(f'입력한 번호: {selected}')





















