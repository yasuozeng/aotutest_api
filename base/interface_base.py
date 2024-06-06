from flask import json

from base import mysql_base
import logging
import mysql.connector
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from mysql.connector import Error


def interface_add(connection,new_data):
    #数据库新增接口
    try:
        cursor = connection.cursor()
        # 构建参数化的SQL语句，使用%形式的参数化查询来防止SQL注入

        sql = """
        INSERT
        INTO
        `interface`(`project_id`, `name`,url,method,type)
        VALUES(%s,%s,%s,%s,%s);
        """
        # 执行SQL更新
        logging.info(f'sql:{sql}')
        cursor.execute(sql, new_data)
        connection.commit()
        logging.info("数据库写入接口成功")
    except Error as e:
        logging.info(f"数据库写入接口失败，错误信息: {e}")
        connection.rollback()

def interface_delete(connection,new_data):
    #数据库新增接口
    try:
        cursor = connection.cursor()
        # 构建参数化的SQL语句，使用%形式的参数化查询来防止SQL注入

        sql = """
            DELETE FROM interface WHERE project_id = %s AND name = %s;
        """
        # 执行SQL更新
        logging.info(f'sql:{sql}')
        cursor.execute(sql, new_data)
        connection.commit()
        logging.info("数据库删除接口成功")
    except Error as e:
        logging.info(f"数据库删除接口失败，错误信息: {e}")
        connection.rollback()

def interface_list(connection,project_id):
    #查询接口列表
    try:
        cursor = connection.cursor()
        sql = """
            SELECT * FROM interface WHERE project_id = %s;
        """
        cursor.execute(sql, (project_id,))
        # 获取查询结果
        interface_list = cursor.fetchall()
        logging.info(f"查询接口列表成功，共找到 {len(interface_list)} 条记录:{interface_list}")
        return interface_list
    except Error as e:
        logging.error(f"查询接口列表失败，错误信息: {e}")
        connection.rollback()

def interface_update(connection,new_data):
    #更新接口数据
    try:
        cursor = connection.cursor()
        # 构建参数化的SQL语句，使用%形式的参数化查询来防止SQL注入
        sql = """
        UPDATE `interface`
        SET
            `name` = %s,
            `url` = %s,
            `method` = %s,
            `type` = %s
        WHERE
            `project_id` = %s AND `name` = %s;
        """
        # 执行SQL更新

        sql_cursor= cursor.execute(sql, new_data)
        logging.info(f"sql_cursor:{sql_cursor}")
        logging.info(f'sql: {sql} with data: {new_data}')
        connection.commit()
        logging.info("接口更新成功")
    except Error as e:
        logging.info(f"接口更新失败，错误信息: {e}")
        connection.rollback()

def interface_details(connection,new_data):
    #查询接口详情
    try:
        cursor = connection.cursor()
        sql = """
            SELECT * FROM interface WHERE project_id = %s and name = %s;
        """
        cursor.execute(sql,new_data)
        # 获取查询结果
        interface_list = cursor.fetchall()
        logging.info(f"查询接口列表成功，共找到 {len(interface_list)} 条记录:{interface_list}")
        return interface_list
    except Error as e:
        logging.error(f"查询接口列表失败，错误信息: {e}")
        connection.rollback()


# if __name__=="__main__":
#     # connect = mysql_base.connect_database()
#     # project_id=24
#     # interface_list(connect, project_id)
#     # mysql_base.disconnect_database(connection=connect)
#
#     # connect = mysql_base.connect_database()
#     # values = (
#     #     '24接口24',
#     #     '/ww1/s',
#     #     'POST',
#     #     '1',
#     #     '24',
#     #     '7',
#     # )
#     # interface_update(connect,values)
#     # mysql_base.disconnect_database(connection=connect)
#
#
#     values = (
#         24,
#         '24接口',
#         '/ww/s',
#         'POST',
#         '1',
#     )
#     connect = mysql_base.connect_database()
#     interface_add(connect, values)
#     mysql_base.disconnect_database(connection=connect)

    # values = (
    #     25,
    #     '25接口',
    # )
    # connect = mysql_base.connect_database()
    # interface_delete(connect, values)
    # mysql_base.disconnect_database(connection=connect)

