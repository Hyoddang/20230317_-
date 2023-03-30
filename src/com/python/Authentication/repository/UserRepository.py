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
                u.user_id,
                u.username,
                u.password,
                u.name,
                u.email,
                ud.phone,
                ud.address,
                ud.gender
            from
                user u
                left outer join user_detail ud on(ud.user_id = u.user_id);
            where
                u.username = %s
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


    @classmethod
    def updateUserDetail(cls, userDetail):
        connection = DBConnectionConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = '''
            update user_detail
            set
                phone = %s,
                address = %s,
                gender = %s
            where
                user_id = %s
        '''
        cursor.execute(sql, (userDetail.phone, userDetail.address, userDetail.gender, userDetail.userId))
        connection.commit()

    @classmethod
    def getUsers(cls):
        connection = DBConnectionConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
                    select
                        u.user_id,
                        u.username,
                        u.password,
                        u.name,
                        u.email,
                        ud.phone,
                        ud.address,
                        ud.gender
                    from
                        user u
                        left outer join user_detail ud on(ud.user_id = u.user_id);
                '''
        cursor.execute(sql)
        rs = cursor.fetchall()

        return rs




if __name__ == '__main__':
    print(UserRepository.getUsers())

