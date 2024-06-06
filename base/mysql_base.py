import logging
import mysql.connector
from mysql.connector import Error


host='localhost'
user='root'
password='123456'
database='aotutest_database'


# 配置日志记录
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def select_database(connection=None,sql=None):
    # 查数据库
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            # 执行 SQL 查询
            cursor.execute(f"{sql}")
            record = cursor.fetchall()
            logging.info('查询成功')
            return record
    except Error as e:
        logging.error("查询失败，错误信息: %s", e)
        return None

def insert_database(connection=None,sql=None):
    # 新增、删除数据库
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            # 执行 SQL 删除
            cursor.execute(f"{sql}")
            connection.commit()  # 提交
            logging.info('操作成功')
    except Error as e:
        logging.error("删除失败，错误信息: %s", e)

def connect_database(host='localhost', user='root', password='123456', database='aotutest_database'):
    # 连接数据库
    try:
        # 连接到 MySQL 数据库
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            logging.info("连接成功")
            return connection
    except Error as e:
        logging.error("连接失败，错误信息: %s", e)
        return None

def disconnect_database(connection=None):
    # 关闭数据库连接
    try:
        # 关闭数据库连接
        if connection.is_connected():
            connection.close()
            logging.info("MySQL 连接已关闭")
    except Error as e:
        logging.error("关闭连接失败，错误信息: %s", e)





if __name__ == "__main__":
    # a = insert_database(sql="INSERT INTO project (name) VALUES ('项目4');")
    # print(a)
    a= connect_database()
    insert_database(connection=a, sql="INSERT INTO project (name) VALUES ('{name1}')")
    c = select_database(connection=a, sql='select * from project')
    print(c)
    b = insert_database(connection=a,sql="DELETE FROM project WHERE name = '{name1}'")
    print(b)
    c = select_database(connection=a,sql='select name,id from project')
    print(c)
    disconnect_database(connection=a)