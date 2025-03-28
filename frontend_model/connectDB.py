import pymysql
import pymysql.cursors

#Prueba2
# Use this to access database
class Dbconnect:
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='sql5.freesqldatabase.com',
                                          db='sql5768755', port=3306, user='sql5768755', password='D62aLxSQtA')
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return result

    def execute(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.connection.commit()
