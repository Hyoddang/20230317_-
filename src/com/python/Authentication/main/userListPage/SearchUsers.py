from src.com.python.Authentication.repository.UserRepository import UserRepository

class SearchUsers:

    @staticmethod
    def searchusers():
        print("====<< 통합검색 >>====")
        searchValue = input("검색어를 입력하세요. : ")
        usersDictList = UserRepository.searchUsers(searchValue)
        print(f'{"ID":<8s}{"사용자이름":<8s}{"성명":<8s}{"이메일":<20s}{"연락처":<16s}{"주소":<20s}성별')
        for userDict in usersDictList:
            print(userDict)
            print(f'{userDict.get("user_id"):<8d}{userDict.get("username"):<8s}{userDict.get("name"):<8s}{userDict.get("email"):<20s}{str(userDict.get("phone")):<16s}{str(userDict.get("address")):<20s}{str(userDict.get("gender"))}')


if __name__ == "__main__":
    SearchUsers.searchusers()