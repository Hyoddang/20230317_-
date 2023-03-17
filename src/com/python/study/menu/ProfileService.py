from src.com.python.study.menu.ProfileRepository import ProfileRepository
from src.com.python.study.menu.UserEntity import UserEntity

class ProfileService:

    @staticmethod
    def addUser():
        print('[사용자 등록 시작]')
        username = input('사용자이름을 입력 하세요.: ')
        password = input('비밀번호를 입력 하세요.: ')
        name = input('성명을 입력 하세요.: ')
        email = input('이메일을 입력 하세요.: ')
        userEntity = UserEntity(username, password, name, email)
        ProfileRepository.insertUser(userEntity)
        print(f'등록된 사용자 정보>>> {userEntity}')
        print('====<< 사용자 등록 완료 >>====')
        print()

    @staticmethod
    def showUserAll():
        print('[사용자 전체 조회]')
        userList = ProfileRepository.selectAllUser()
        for user in userList:
            print(user)
        print('====<< 사용자 전체 조회 완료 >>====')
        print()