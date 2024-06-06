from base import mysql_base
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def project_list(connection):
    #查询数据库中的项目
    project_list_sql = "SELECT name, id FROM project ORDER BY created_time DESC "
    project_list = mysql_base.select_database(connection=connection,sql=project_list_sql)
    logging.info(f'{project_list}')
    return project_list

def project_add(connection,name=None):
    #新增项目
    project_list_sql = f"INSERT INTO project (name) VALUES ('{name}')"
    logging.info(f'{project_list_sql}')
    project_list = mysql_base.insert_database(connection=connection,sql=project_list_sql)
    logging.info(f'{project_list}')

def project_delete(connection,name=None):
    #删除项目
    project_list_sql = f"DELETE FROM project WHERE name = '{name}'"
    logging.info(f'{project_list_sql}')
    project_list = mysql_base.insert_database(connection=connection,sql=project_list_sql)
    logging.info(f'{project_list}')


if __name__ == "__main__":

    connect=mysql_base.connect_database()
    project_list(connection=connect)
    print(project_list(connection=connect))
    project_add(connection=connect, name='5656')
    # print(project_add(connection=connect, name='5656'))
    project_list(connection=connect)
    print(project_list(connection=connect))
    # project_delete(connection=connect, name='5656')
    # print(project_delete(connection=connect, name='5656'))
    # project_list(connection=connect)
    # print(project_list(connection=connect))
    mysql_base.disconnect_database(connection=connect)





