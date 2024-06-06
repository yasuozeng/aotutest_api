import logging

from base import mysql_base

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def select_project_id_name(project_name):
    #接收项目名称，查库，返回项目id和name,第一个是id，第二个是name
    try:
        connect = mysql_base.connect_database()  # 链接数据库
        sql = f'SELECT id FROM project where name = "{project_name}";'
        logging.info(f'sql:{sql}')
        project_id = mysql_base.select_database(connection=connect, sql=sql)
        logging.info(f'project_id:{project_id}')
        project_list = []
        logging.info(f'project_list:{project_list}')
        project_list.append(project_id[0][0],)
        project_list.append(project_name)
        mysql_base.disconnect_database(connection=connect)
        return project_list
    except Exception as e:
        logging.error("查询失败，错误信息: %s", e)
        return None


if __name__ == '__main__':
    a = select_project_id_name(project_name= '004')
    print(a)