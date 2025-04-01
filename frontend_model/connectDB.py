import pymysql
import pymysql.cursors

#TODO: H
class Dbconnect:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host='mysql-f718405-pedro.l.aivencloud.com',
            db='defaultdb',
            port=24211,
            user='avnadmin',
            password='AVNS_hHeZnyU4Z0cK8LDHs5O',
            cursorclass=pymysql.cursors.DictCursor  
        )
        self.cursor = self.connection.cursor()

    def select(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.connection.commit()
