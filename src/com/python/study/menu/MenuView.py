class MenuView:

    @staticmethod
    def getMainMenu():
        menuStr = '''[메인 메뉴]
1. 프로필 조회
2. 프로필 등록
3. 프로필 수정
4. 프로필 삭제'''
        return menuStr

    @staticmethod
    def getSelectProfileMenu():
        menuStr = '''[프로필 조회 메뉴]
1. 전체 조회
2. 사용자 이름으로 조회
'''
        return menuStr

    @staticmethod
    def getAddProfileMenu():
        menuStr = '''[프로필 등록 메뉴]
1. 사용자 등록
'''
        return menuStr

    @staticmethod
    def getExitMenu():
        return 'q. 프로그램 종료'

    @staticmethod
    def getBackMenu():
        return 'b. 뒤로가기'