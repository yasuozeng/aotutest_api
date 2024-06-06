import logging
from mysql.connector import Error

from base import mysql_base


def scene_add(connection, values):
    # 新增 scene
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO testscene (project_name, name) VALUES(%s, %s);
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库写入scene成功")
    except Error as e:
        logging.error(f"数据库写入scene失败，错误信息: {e}")
        connection.rollback()

def scene_delete(connection, scene_name):
    # 删除 scene
    try:
        cursor = connection.cursor()
        sql = """
        DELETE FROM testscene WHERE name = %s;
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, (scene_name,))
        connection.commit()
        logging.info("数据库删除scene成功")
    except Error as e:
        logging.error(f"数据库删除scene失败，错误信息: {e}")
        connection.rollback()

def scene_list(connection, project_name):
    # 查询 scene 列表
    try:
        cursor = connection.cursor()
        sql = """
        SELECT * FROM testscene WHERE project_name = %s;
        """
        cursor.execute(sql, (project_name,))
        scene_list = cursor.fetchall()
        logging.info(f"查询scene列表成功，共找到 {len(scene_list)} 条记录: {scene_list}")
        return scene_list
    except Error as e:
        logging.error(f"查询scene列表失败，错误信息: {e}")
        connection.rollback()

def scene_update(connection, values):
    # 更新 scene
    try:
        cursor = connection.cursor()
        sql = """
        UPDATE testscene SET name = %s WHERE name = %s;
        """
        logging.info(f'sql: {sql}')
        cursor.execute(sql, values)
        connection.commit()
        logging.info("数据库更新scene成功")
    except Error as e:
        logging.error(f"数据库更新scene失败，错误信息: {e}")
        connection.rollback()

# if __name__=='__main__':
#     project_id=29
#     connect = mysql_base.connect_database()
#     scene_list(connect, project_id)
#     mysql_base.disconnect_database(connection=connect)

    # values=(
    #     29,
    #     'zhuce'
    # )
    # connect = mysql_base.connect_database()
    # scene_add(connect,values)
    # mysql_base.disconnect_database(connection=connect)

    # values=(
    #     '66',
    #     4
    # )
    # connect = mysql_base.connect_database()
    # scene_update(connect, values)
    # mysql_base.disconnect_database(connection=connect)

    # testscene_id=4
    # connect = mysql_base.connect_database()
    # scene_delete(connect, testscene_id)
    # mysql_base.disconnect_database(connection=connect)

