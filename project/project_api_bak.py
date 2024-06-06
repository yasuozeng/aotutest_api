import logging

from project import project_base
from flask import Flask, jsonify, request
from base import mysql_base

app = Flask(__name__)

# 示例数据

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# 定义路由，创建接口
@app.route('/project_list', methods=['GET'])                    #用于创建路由的装饰器
def project_list():
    #查询项目名字列表
    connect = mysql_base.connect_database()                 #链接数据库
    data = project_base.project_list(connection=connect)                    #获取查询数据库返回值
    unique_values = []                  #筛选出项目名字
    for item in data:
        unique_values.append(item[0])
    mysql_base.disconnect_database(connection=connect)                  #关闭数据库
    logging.info(unique_values)
    # return jsonify(list(unique_values))
    return unique_values

@app.route('/project_add', methods=['POST'])                    #用于创建路由的装饰器
def project_add():
    #新增项目
    # 获取 POST 请求的 JSON 数据
    data = request.json
    connect = mysql_base.connect_database()                 #链接数据库
    name = data.get('name')
    project_base.project_add(connection=connect,name=name)                    #执行新增数据库返回值
    data = project_base.project_list(connection=connect)    # 获取查询数据库返回值
    unique_values = []      # 筛选出项目名字
    logging.info(unique_values)
    for item in data:
        unique_values.append(item[0])
    if name in unique_values:
        add_success = '新建项目成功'
        return  add_success
    else:
        add_fail = '新建项目失败'
        return add_fail

@app.route('/project_delete', methods=['POST'])                    #用于创建路由的装饰器
def project_delete():
    #查询项目名字列表
    # 获取 POST 请求的 JSON 数据
    data = request.json
    connect = mysql_base.connect_database()                 #链接数据库
    name = data.get('name')
    logging.info(f"接收到的值：{name}")
    project_base.project_delete(connection=connect,name=name)                    #执行删除数据库返回值
    data = project_base.project_list(connection=connect)    # 获取查询数据库返回值
    unique_values = []      # 筛选出项目名字
    logging.info(unique_values)
    for item in data:
        unique_values.append(item[0])
    if name in unique_values:
        delete_success = '删除项目失败'
        return  delete_success
    else:
        delete_fail = '删除项目成功'
        return delete_fail




if __name__ == '__main__':
    # project_list()
    app.run(debug=True)
