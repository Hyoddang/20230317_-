import pymysql.cursors
from src.com.python.Authentication.config.DBConnectionConfig import DBConnectionConfig

class UserRepository:


    @classmethod
    def saveUser(cls, user):
        connection = DBConnectionConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
            insert into user
            values (0, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (user.username, user.password, user.name, user.email))
        connection.commit()

    @classmethod
    def findUserByUsername(cls, username):
        connection = DBConnectionConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
            select
                user_id,
                username,
                password,
                name,
                email
            from
                user
            where
                username = %s
        '''
        cursor.execute(sql, (username, ))
        rs = cursor.fetchone()

        return rs

    @classmethod
    def getUsers(cls):
        pass

    @classmethod
    def updateUser(cls, user):
        connection = DBConnectionConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = '''
            update user
            set
                password = %s,
                name = %s,
                email = %s
            where
                username = %s
        '''
        cursor.execute(sql, (user.password, user.name, user.email, user.username))
        connection.commit()                   ## 데이터가 업데이트 되었다는걸 적용하는 명령어 필수*

    @classmethod
    def removeUserByUsername(cls, username):
        connetion = DBConnectionConfig.getConnection()
        cursor = connetion.cursor(pymysql.cursors.DictCursor)
        sql ='''
            delete
            from
                user
            where
                username = %s
        '''
        cursor.execute(sql, (username, ))
        connetion.commit()

if __name__ == '__main__':
    UserRepository.findUserByUsername('qwe')





