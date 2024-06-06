from flask import json

from base import mysql_base
import logging
import mysql.connector
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from mysql.connector import Error


def intercase_add(connection, values):
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO InterCase (project_name, title, interface_id, headers, request, file, setup_script, teardown_script) 
            VALUES  (%s, %s, %s, %s, %s, %s, %s,%s)
            """
            cursor.execute(sql, values)
        connection.commit()
        logging.info('新增用例成功')
    except Exception as e:
        connection.rollback()
        raise e

def intercase_delete(connection, intercase_id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM InterCase WHERE title = %s"
            cursor.execute(sql, (intercase_id,))
        connection.commit()
        logging.info('删除用例成功')
    except Exception as e:
        connection.rollback()
        raise e

def intercase_list(connection, project_name):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM InterCase WHERE project_name = %s"
            cursor.execute(sql, (project_name,))
            return cursor.fetchall()
            logging.info('查询用例成功')
    except Exception as e:
        raise e

def intercase_update(connection, values):
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE InterCase
            SET project_name = %s, title = %s, interface_id = %s, headers = %s, request = %s, file = %s, setup_script = %s, teardown_script = %s
            WHERE title = %s
            """
            cursor.execute(sql, values)
        connection.commit()
        logging.info('修改用例成功')
    except Exception as e:
        connection.rollback()
        raise e


def intercase_details(connection, values):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM InterCase WHERE project_name = %s and title= %s"
            cursor.execute(sql, values)
            return cursor.fetchall()
            logging.info('查询用例成功')
    except Exception as e:
        raise e



# if __name__=='__main__':
#     # values = (
#     #     '自动化测试平台项目新增用例',
#     #     '2',
#     #     json.dumps({}),
#     #     json.dumps({'name':'test项目新增'}),
#     #     json.dumps({}),
#     #     '',
#     #     ''
#     #
#     # )
#     # connect = mysql_base.connect_database()
#     # intercase_add(connect, values)
#     # mysql_base.disconnect_database(connection=connect)
#
#     # intercase_id=1
#     # connect = mysql_base.connect_database()
#     # intercase_delete(connect, intercase_id)
#     # mysql_base.disconnect_database(connection=connect)
#
#     # project_id=29
#     # connect = mysql_base.connect_database()
#     # a= intercase_list(connect, project_id)
#     # print(a)
#     # mysql_base.disconnect_database(connection=connect)
#
#     values = (
#         '1自动化测试平台项目新增用例',
#         '2',
#         json.dumps({}),
#         json.dumps({'name':'test项目新增'}),
#         json.dumps({}),
#         '',
#         '',
#         2,
#     )
#     connect = mysql_base.connect_database()
#     intercase_update(connect, values)
#     mysql_base.disconnect_database(connection=connect)