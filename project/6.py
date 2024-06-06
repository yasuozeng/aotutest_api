import logging
import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host='localhost', user='root', password='123456', database='aotutest_database'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

        # 配置日志记录
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    def connect(self):
        try:
            # 连接到 MySQL 数据库
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                logging.info("连接成功")
        except Error as e:
            logging.error("连接失败，错误信息: %s", e)

    def disconnect(self):
        try:
            # 关闭数据库连接
            if self.connection is not None and self.connection.is_connected():
                self.connection.close()
                logging.info("MySQL 连接已关闭")
        except Error as e:
            logging.error("关闭连接失败，错误信息: %s", e)

    def select(self, sql):
        # 查数据库
        try:
            if self.connection is not None and self.connection.is_connected():
                cursor = self.connection.cursor()
                # 执行 SQL 查询
                cursor.execute(sql)
                record = cursor.fetchall()
                logging.info('查询成功')
                return record
        except Error as e:
            logging.error("查询失败，错误信息: %s", e)
            return None

    def insert(self, sql):
        # 新增、删除数据库
        try:
            if self.connection is not None and self.connection.is_connected():
                cursor = self.connection.cursor()
                # 执行 SQL 删除
                cursor.execute(sql)
                self.connection.commit()  # 提交
                logging.info('操作成功')
        except Error as e:
            logging.error("删除失败，错误信息: %s", e)

# 使用示例
# 创建 MySQLDatabase 实例
db = MySQLDatabase()

# 连接数据库
db.connect()

# 执行查询操作
result = db.select("SELECT * FROM project")

# 执行插入操作
db.insert("INSERT INTO project (name) VALUES ('{name1}')")

# 断开数据库连接
db.disconnect()
