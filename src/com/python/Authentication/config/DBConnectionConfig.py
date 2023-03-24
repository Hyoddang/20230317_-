import pymysql


class DBConnectionConfig:
    host = '127.0.0.1'           # 자기 자신의 주소
    port = 3306                  # 데이터베이스 서버의 포트번호
    user = 'root'                # 사용자 이름
    password = 'root'            # 비밀번호
    database = 'python_auth'     # 연결할 데이터 베이스 명

    instance = None              #Connection객체를 담을 변수

    @classmethod
    def getConnection(cls):
        if cls.instance == None:
            cls.instance = pymysql.connect(
                host=cls.host,
                port=cls.port,
                user=cls.user,
                password=cls.password,
                database=cls.database
            )
        return cls.instance

