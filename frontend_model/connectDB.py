import pymysql
import pymysql.cursors


# Use this to access database
class Dbconnect:
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='mysql-f718405-pedro.l.aivencloud.com',
                                          db='defaultdb', port=24211, user='avnadmin', password='AVNS_hHeZnyU4Z0cK8LDHs5O')
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