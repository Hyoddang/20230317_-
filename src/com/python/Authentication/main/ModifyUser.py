from src.com.python.Authentication.security.PrincipalUser import PrincipalUser
from src.com.python.Authentication.repository.UserRepository import UserRepository
from src.com.python.Authentication.entity.User import User

class ModifyUser:

    @staticmethod
    def modifyUser():
        select = input("회원정보 수정에 동의 하십니까? 계속 하려면 (Y/y) 입력, 취소 하려면 아무키나 입력 : ")
        if select != 'Y' and select != 'y':
            return

        checkPassword = input("기존 비밀번호를 입력 해주세요. : ")
        if PrincipalUser.session.get('password') != checkPassword:
            print('비밀번호를 다시 확인 해주세요.')
            return

        while True:
            print("=====<< ModifyUser >>=====")
            print("1. 기본정보 수정")
            print("2. 비밀번호 수정")
            print("b. 뒤로가기")
            print("====================")
            select = input("Menu Selected : ")
            if select == 'b':
                break
            elif select == '1':
                ModifyUser.updateBasicInformation()
            elif select == '2':
                ModifyUser.updatePassword()
            else:
                print("잘못 입력 하셨습니다.")
                print("====================")
                print()

    @staticmethod
    def updateBasicInformation():
        print('수정하지 않으려면 공백을 남겨주세요.')
        name = input('name : ')
        email = input('email : ')

        if len(name.replace(' ', '') + email.replace(' ', '')) == 0:
            print('수정 사항이 없습니다.')
            return


        userDict = PrincipalUser.session
        user = User(
            userDict.get('username'),
            userDict.get('password'),
            name if len(name.replace(' ', '')) > 0 else userDict.get('name'),
            email if len(email.replace(' ', '')) > 0 else userDict.get('email'),
            )

        UserRepository.updateUser(user)
        PrincipalUser.setSession(UserRepository.findUserByUsername(user.username))
        print('회원정보 수정에 성공하였습니다.')

    # @staticmethod
    # def updatePassword():
    #     select = input("비밀번호 변경에 동의 하십니까? 계속 하려면 (Y/y) 입력, 취소 하려면 아무키나 입력 : ")
    #     if select != 'Y' and select != 'y':
    #         return
    #     userDict = PrincipalUser.session
    #     loopFlag = True
    #     newPassword = None
    #
    #     while loopFlag:
    #         newPassword = input('변경할 비밀번호를 입력하세요. : ')
    #         if len(newPassword) > 7:
    #             while True:
    #                 if newPassword != userDict.get('password'):
    #                     checkPassword = input('비밀번호를 한번 더 입력 해주세요. : ')
    #                     if newPassword == checkPassword:
    #                         loopFlag = False
    #                         print('변경 되었습니다.')
    #                     break
    #
    #                 userDict = PrincipalUser.session
    #                 user = User(
    #                     userDict.get('username'),
    #                     userDict.get('password'),
    #                     userDict.get('name'),
    #                     userDict.get('email')
    #                 )
    #         # UserRepository.updateUser(newPassword)
    #         # PrincipalUser.setSession(UserRepository.)





        '''
        newPassword 새로운 비밀번호 입력
        비밀번호가 8자 이상인지 확인
        기존의 비밀번호와 다른지 확인
        두 조건이 성립되지 않으면 다시 newPassword를 입력 받도록 한다.
        
        checkPassword 새로운 비밀번호 확인 입력
        newPassword와 일치하는지 확인
        일치하지 않으면 다시 newPassword를 입력하도록 한다.
        
        모든 조건이 성립되면 updateUser를 호출하여 새로운 비밀번호를 commit한다.
        update된 정보를 다시 principal에 저장한다.
        비밀번호 변경 완료되었습니다. 메세지 출력
        '''

    @staticmethod
    def updatePassword():
        select = input("비밀번호 변경에 동의 하십니까? 계속 하려면 (Y/y) 입력, 취소 하려면 아무키나 입력 : ")
        if select != 'Y' and select != 'y':
            return

        newPassword = None

        while True:
            newPassword = input('변경할 비밀번호를 입력하세요. : ')
            if len(newPassword) < 8:
                print("비밀번호는 8자 이상이어야 합니다.")
                continue
            if PrincipalUser.session.get('password') == newPassword:
                print("기존 비밀번호와 동일한 비밀번호는 사용할 수 없습니다.")
                continue
            checkPassword = input("비밀번호를 한번 더 입력해주세요. : ")
            if checkPassword != newPassword:
                print("비밀번호를 다시 입력해주세요.")
                continue

            userDict = PrincipalUser.session
            user = User(
                userDict.get('username'),
                    newPassword,
                    userDict.get('name'),
                    userDict.get('email')
                )
            UserRepository.updateUser(user)
            PrincipalUser.setSession(UserRepository.findUserByUsername(user.username))
            print('비밀번호가 변경이 완료 되었습니다.')
            return



















