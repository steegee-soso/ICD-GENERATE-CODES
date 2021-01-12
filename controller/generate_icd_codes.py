from controller.config import *
import os

db = DbMysql()


class GenerateIcDCode:
    flag = False

    def __init__(self):
        connection = db.connector()
        my_cursor = connection.cursor()
        pass

    def get_all_icd_code_type(self):
        connection = db.connector()
        my_cursor = connection.cursor()
        fetch = ()

        sql = "Select * from icd_records"

        try:
            my_cursor.execute(sql)
            fetch = my_cursor.fetchall()
        except Exception as e:
            print(e)
            print("Log the errors")
        finally:
            my_cursor.close()
            connection.close()
        return fetch

        pass

    def count_all_record(self):

        connection = db.connector()
        my_cursor = connection.cursor()
        fetch = 0

        sql = "Select count(*) as total from icd_codes"

        try:
            my_cursor.execute(sql)
            fetch = my_cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            my_cursor.close()
            connection.close()
        return fetch

    def create_icd_code(self, category_code,
                        icd_diagnosis_code,
                        full_icd_code, abbreviated_description,
                        full_description, category_title, icd_type_id):

        connection = db.connector()
        my_cursor = connection.cursor()

        flag = False
        result = 0

        data = (f'{category_code}', f'{icd_diagnosis_code}', f'{full_icd_code}', f'{abbreviated_description}',
                f'{full_description}', f'{category_title}', f'{icd_type_id}')

        sql = """INSERT INTO icd_codes(category_code,icd_diagnosis_code,
          full_icd_code, abbreviated_description,full_description,category_title,icd_type_id) 
         VALUE(%s,%s,%s,%s,%s,%s,%s)"""

        try:
            my_cursor.execute(sql, data)
            connection.commit()
            result = my_cursor.lastrowid

            if result > 0:
                flag = True
            else:
                flag = False

        except Exception as e:
            print(e)
            my_cursor.close()
            connection.close()
        finally:
            my_cursor.close()
            connection.close()
        return flag

    def list_all_codes(self, start, max_limit):

        connection = db.connector()
        my_cursor = connection.cursor()
        fetch = ()

        params = (start, max_limit,)

        sql_one = """Select c.category_code, c.icd_diagnosis_code,c.full_icd_code, 
        c.abbreviated_description, c.status,c.full_description,	c.category_title,
        ic.icd_name, c.id  from icd_codes c JOIN icd_records ic  
        ON c.icd_type_id=ic.id LIMIT %s,%s """

        try:
            my_cursor.execute(sql_one, params)
            fetch = my_cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            my_cursor.close()
            connection.close()
        return fetch
        pass

    def update_all_codes(self, category_code, icd_diagnosis_code,
                         full_icd_code, abbreviated_description,
                         full_description, category_title, icd_type_id, id):

        connection = db.connector()
        my_cursor = connection.cursor()

        sql = """ UPDATE icd_codes set category_code=%s,icd_diagnosis_code=%s, 
        full_icd_code=%s, abbreviated_description=%s, full_description=%s,
        category_title=%s ,icd_type_id=%s 
        WHERE id=%s """

        result = 0

        data = (f'{category_code}', f'{icd_diagnosis_code}', f'{full_icd_code}', f'{abbreviated_description}',
                f'{full_description}', f'{category_title}', f'{icd_type_id}', id)

        print(data)

        try:
            my_cursor.execute(sql, data)
            connection.commit()
            result = my_cursor.rowcount
        except Exception as e:
            print(e)
            connection.rollback()
        finally:
            my_cursor.close()
            connection.close()
        return result
        pass

    def delete_icd_code(self, id):
        flag = False
        connection = db.connector()
        my_cursor = connection.cursor()
        result = 0

        sql = "Update icd_codes set status=%s where id=%s"
        update_record = ("inactive", int(id))

        try:

            my_cursor.execute(sql, update_record)
            connection.commit()
            result = my_cursor.rowcount

            if result > 0:
                flag = True
        except Exception as e:
            print(e)
        finally:
            my_cursor.close()
            connection.close()
        return flag

    def fetch_one_record(self, id):

        connection = db.connector()
        my_cursor = connection.cursor()
        fetch = ()

        sql = """Select c.category_code, c.icd_diagnosis_code,c.full_icd_code, 
        c.abbreviated_description, c.status,c.full_description,	c.category_title,
        ic.icd_name,count(*) as num from icd_codes c JOIN icd_records ic  
        ON c.icd_type_id=ic.id where c.id=%s"""

        try:
            my_cursor.execute(sql, (id,))
            fetch = my_cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            my_cursor.close()
            connection.close()
        return fetch

    def code_exist(self, id):

        flag = False
        connection = db.connector()
        my_cursor = connection.cursor()
        fetch = ()

        sql = "Select count(*) as num from icd_codes where id = %s"
        try:
            my_cursor.execute(sql, (id,))
            fetch = my_cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            my_cursor.close()
            connection.close()
        return fetch

    def process_all_records(self, fetch_one):

        list_data = []

        if len(fetch_one) == 1:

            record = {"category_code": fetch_one[0],
                      "diagnosis_code": fetch_one[1],
                      "full_icd_code": fetch_one[2],
                      "abbreviated_description": fetch_one[3],
                      "status":fetch_one[4],
                      "full_description": fetch_one[5],
                      "category_title": fetch_one[6],
                      "icd_type": fetch_one[7],
                      "id": fetch_one[8]
                      }
            return record
        else:
            for data in fetch_one:
                record = {}
                record["category_code"] = data[0]
                record["diagnosis_code"] = data[1]
                record["full_icd_code"] = data[2]
                record["abbreviated_description"] = data[3]
                record['status']=data[4]
                record["full_description"] = data[5]
                record["category_title"] = data[6]
                record["icd_type"] = data[7]
                record['id'] = data[8]
                list_data.append(record)
        return list_data

    def is_icd_exists(self, icd_code):
        connection = db.connector()
        my_cursor = connection.cursor()
        fetch = ()

        sql = "Select count(*) as num from icd_codes where full_icd_code=%s"

        try:
            my_cursor.execute(sql, (f'{icd_code}',))
            fetch = my_cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            my_cursor.close()
            connection.close()
        return fetch
        pass


