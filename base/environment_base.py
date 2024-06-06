from flask import json

from base import mysql_base
import logging
import mysql.connector
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from mysql.connector import Error
def environment_name_id_list(connection,project_id):
    #查询数据库中的环境name,id
    environment_list_sql = f"SELECT name,id FROM environment where project_id={project_id} ORDER BY id DESC "
    environment_list = mysql_base.select_database(connection=connection,sql=environment_list_sql)
    logging.info(f'{environment_list}')
    return environment_list

def environment_list(connection,project_id,environment_name):
    #查询数据库中的环境name,id
    environment_list_sql = f"SELECT * FROM environment where project_id={project_id} and name='{environment_name}' ORDER BY id DESC "
    environment_list = mysql_base.select_database(connection=connection,sql=environment_list_sql)
    logging.info(f'{environment_list}')
    return environment_list

def environment_add(connection,name=None,project_id=None):
    #新增环境
    #sql模板
    environment_add_sql = f"INSERT INTO `environment` (`name`,`project_id`) VALUES ('{name}',{project_id});"
    logging.info(f'{environment_add_sql}')
    environment_add = mysql_base.insert_database(connection=connection,sql=environment_add_sql)
    logging.info(f'{environment_add}')

def environment_delete(connection,name=None,project_id=None):
    #删除环境
    environment_delete_sql = f"DELETE FROM environment WHERE project_id = {project_id} AND name = '{name}';"
    logging.info(f'{environment_delete_sql}')
    environment_delete = mysql_base.insert_database(connection=connection,sql=environment_delete_sql)
    logging.info(f'{environment_delete}')
    success_message = {"message": "删除环境成功"}

    return success_message  # 返回JSON响应和HTTP状态码

def environment_update(connection, project_id, environment_id, new_data):
    """
    更新环境配置信息
    :param connection: 数据库连接对象
    :param project_id: 项目ID
    :param environment_id: 环境ID
    :param new_data: 包含更新数据的字典
    """
    try:
        cursor = connection.cursor()
        # 构建参数化的SQL语句，使用%形式的参数化查询来防止SQL注入
        sql = """
        UPDATE `environment`
        SET
            `name` = %s,
            `global_variable` = %s,
            `debug_global_variable` = %s,
            `db` = %s,
            `host` = %s,
            `headers` = %s,
            `global_func` = %s
        WHERE
            `project_id` = %s AND `id` = %s;
        """
        # 执行SQL更新
        cursor.execute(sql, new_data)
        connection.commit()
        print("环境配置更新成功")
    except Error as e:
        print(f"更新环境配置失败，错误信息: {e}")
        connection.rollback()


def environment_id(connection,project_id,environment_name):
    #查询数据库中的环境name,id
    environment_list_sql = f"SELECT name,id FROM environment where project_id={project_id} AND name='{environment_name}' ORDER BY id DESC "
    logging.info(f"environment_list_sql:{environment_list_sql}")
    environment_id = mysql_base.select_database(connection=connection,sql=environment_list_sql)
    logging.info(f'{environment_id}')
    return environment_id

# if __name__=='__main__':
#     connect=mysql_base.connect_database()
#     # # environment_add(connect, name=333, project_id=25)
#     # # environment_name_id_list(connect, 25)
#     # # environment_delete(connect, name=333, project_id=25)
#     # # environment_name_id_list(connect, 25)
#     # environment_list(connect, 25)
#     # mysql_base.disconnect_database(connection=connect)
#
#
#     # 准备更新的数据
#     # new_data = {
#     #     'name': 'Updated Environment',
#     #     'global_variable': {'key1': 'new_value1', 'key2': 'new_value2'},
#     #     'debug_global_variable': {'debug_key1': 'new_debug_value1'},
#     #     'db': {'dbname': 'new_dbname', 'user': 'new_user', 'password': 'new_password'},
#     #     'host': 'new_host_address',
#     #     'headers': {'header1': 'new_header_value1', 'header2': 'new_header_value2'},
#     #     'global_func': 'new_global_functions'
#     # }
#     new_data = {
#         'name': '66',
#         'global_variable': None,
#         'debug_global_variable': None,
#         'db':None,
#         'host': None,
#         'headers':None,
#         'global_func': None
#     }
#     project_id = 25
#     environment_id = 4
#
#     # 调用函数更新环境配置
#     update_environment(connect, project_id, environment_id, new_data)
