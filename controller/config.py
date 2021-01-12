import mysql.connector
import time


class DbMysql:

    def __init__(self):
        pass

    def connector(self):
        retries = 8

        while True:
            try:
                return mysql.connector.connect(host="db",port="3306", user="root", password="root", db="icd")
            except Exception as e:
                if retries == 0:
                    raise e
                retries -= 1
                time.sleep(0.20)