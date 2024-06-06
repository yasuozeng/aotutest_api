import logging
from mysql.connector import Error
from base import mysql_base

def report_add(connection, values):
    # 数据库新增 report
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO report (info, record, testtask_id)
        VALUES (%s, %s, %s);
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库新增 report 成功")
    except Error as e:
        logging.error(f"数据库新增 report 失败，错误信息: {e}")
        connection.rollback()

def report_delete(connection, report_id):
    # 数据库删除 report
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM report WHERE id = %s;"
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (report_id,))
        connection.commit()
        logging.info("数据库删除 report 成功")
    except Error as e:
        logging.error(f"数据库删除 report 失败，错误信息: {e}")
        connection.rollback()

def report_list(connection,testtask_id):
    # 数据库查询 report 列表
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM report where testtask_id = %s;"
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (testtask_id,))
        report_list = cursor.fetchall()
        logging.info(f"查询 report 列表成功，共找到 {len(report_list)} 条记录: {report_list}")
        return report_list
    except Error as e:
        logging.error(f"查询 report 列表失败，错误信息: {e}")
        connection.rollback()

def report_update(connection, values):
    # 数据库更新 report
    try:
        cursor = connection.cursor()
        sql = """
        UPDATE report
        SET info = %s, record = %s, testtask_id = %s
        WHERE id = %s;
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库更新 report 成功")
    except Error as e:
        logging.error(f"数据库更新 report 失败，错误信息: {e}")
        connection.rollback()

if __name__=='__main__':
    # values = (
    #     '1',
    #     '1',
    #     1,
    # )
    # connect = mysql_base.connect_database()
    # report_add(connect, values)
    # mysql_base.disconnect_database(connection=connect)

    # testtask_id=1
    # connect = mysql_base.connect_database()
    # report_list(connect, testtask_id)
    # mysql_base.disconnect_database(connection=connect)

    report_id=1
    connect = mysql_base.connect_database()
    report_delete(connect, report_id)
    mysql_base.disconnect_database(connection=connect)


