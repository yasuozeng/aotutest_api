import logging
from mysql.connector import Error

from base import mysql_base


def scenetocase_add(connection, values):
    # 数据库新增 SceneToCase
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO SceneToCase (case_name, scene_name, sort)
        VALUES (%s, %s, %s);
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库新增 SceneToCase 成功")
    except Error as e:
        logging.error(f"数据库新增 SceneToCase 失败，错误信息: {e}")
        connection.rollback()

def scenetocase_delete(connection, scenetocase_name):
    # 数据库删除 SceneToCase
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM SceneToCase WHERE id = %s;"
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (scenetocase_name,))
        connection.commit()
        logging.info("数据库删除 SceneToCase 成功")
    except Error as e:
        logging.error(f"数据库删除 SceneToCase 失败，错误信息: {e}")
        connection.rollback()

def scenetocase_list(connection, scene_name):
    # 数据库查询 SceneToCase 列表
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM SceneToCase WHERE scene_name = %s;"
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (scene_name,))
        scenetocase_list = cursor.fetchall()
        logging.info(f"查询 SceneToCase 列表成功，共找到 {len(scenetocase_list)} 条记录: {scenetocase_list}")
        return scenetocase_list
    except Error as e:
        logging.error(f"查询 SceneToCase 列表失败，错误信息: {e}")
        connection.rollback()

def scenetocase_update(connection, values):
    # 数据库更新 SceneToCase
    try:
        cursor = connection.cursor()
        sql = """
        UPDATE SceneToCase
        SET case_name = %s, scene_name = %s, sort = %s
        WHERE id = %s;
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库更新 SceneToCase 成功")
    except Error as e:
        logging.error(f"数据库更新 SceneToCase 失败，错误信息: {e}")
        connection.rollback()


if __name__=='__main__':
    # values=(
    #     2,
    #     2,
    #     2
    # )
    # connect = mysql_base.connect_database()
    # scenetocase_add(connect, values)
    # mysql_base.disconnect_database(connection=connect)

    # scene_name=1
    # connect = mysql_base.connect_database()
    # scenetocase_list(connect, scene_name)
    # mysql_base.disconnect_database(connection=connect)

    # values=(
    #     1,
    #     1,
    #     4,
    #     1
    # )
    # connect = mysql_base.connect_database()
    # scenetocase_update(connect, values)
    # mysql_base.disconnect_database(connection=connect)

    scenetocase_name=2
    connect = mysql_base.connect_database()
    scenetocase_delete(connect, scenetocase_name)
    mysql_base.disconnect_database(connection=connect)