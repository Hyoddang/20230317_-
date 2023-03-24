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
        pass

    @classmethod
    def removeUserByUsername(cls, username):
        pass


if __name__ == '__main__':
    UserRepository.findUserByUsername('qwe')





