import logging
from mysql.connector import Error

from base import mysql_base


def testtask_add(connection, values):
    # 数据库新增 testtask
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO testtask (project_id, name, scenet_id)
        VALUES (%s, %s, %s);
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库新增 testtask 成功")
    except Error as e:
        logging.error(f"数据库新增 testtask 失败，错误信息: {e}")
        connection.rollback()

def testtask_delete(connection, testtask_id):
    # 数据库删除 testtask
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM testtask WHERE id = %s;"
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (testtask_id,))
        connection.commit()
        logging.info("数据库删除 testtask 成功")
    except Error as e:
        logging.error(f"数据库删除 testtask 失败，错误信息: {e}")
        connection.rollback()

def testtask_list(connection, project_id):
    # 数据库查询 testtask 列表
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM testtask WHERE project_id = %s;"
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (project_id,))
        testtask_list = cursor.fetchall()
        logging.info(f"查询 testtask 列表成功，共找到 {len(testtask_list)} 条记录: {testtask_list}")
        return testtask_list
    except Error as e:
        logging.error(f"查询 testtask 列表失败，错误信息: {e}")
        connection.rollback()

def testtask_update(connection, values):
    # 数据库更新 testtask
    try:
        cursor = connection.cursor()
        sql = """
        UPDATE testtask
        SET project_id = %s, name = %s, scenet_id = %s
        WHERE id = %s;
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库更新 testtask 成功")
    except Error as e:
        logging.error(f"数据库更新 testtask 失败，错误信息: {e}")
        connection.rollback()


if __name__=='__main__':

    # values=(
    #     29,
    #     '自动化测试平台新增项目任务',
    #     1
    # )
    # connect = mysql_base.connect_database()
    # testtask_add(connect, values)
    # mysql_base.disconnect_database(connection=connect)

    # project_id=29
    # connect = mysql_base.connect_database()
    # testtask_list(connect, project_id)
    # mysql_base.disconnect_database(connection=connect)

    # values=(
    #     29,
    #     '88自动化测试平台新增项目任务',
    #     1,
    #     1
    # )
    # connect = mysql_base.connect_database()
    # testtask_update(connect, values)
    # mysql_base.disconnect_database(connection=connect)

    testtask_id=2
    connect = mysql_base.connect_database()
    testtask_delete(connect, testtask_id)
    mysql_base.disconnect_database(connection=connect)