import logging
from flask import Flask, jsonify, request,Blueprint, jsonify
from base import mysql_base,app_base,project_base,environment_base
from flask import json

#创建蓝图
environment_bp = Blueprint('environment' , __name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@environment_bp.route('/environment_name_list',methods=['POST'])
def environment_name_list():
    #环境列表入参：name项目名字
    data = request.json
    name = data.get('name')
    project_id_name = app_base.select_project_id_name(name)  #获取项目的id和名字
    connect = mysql_base.connect_database()
    project_id=project_id_name[0]
    environment_name_id_list=environment_base.environment_name_id_list(connect,project_id)
    environment_list=[]
    for i in  environment_name_id_list:
        logging.info(f"i是：{i[0]}")
        environment_list.append(i[0])
    mysql_base.disconnect_database(connection=connect)
    logging.info(f"environment_list是：{environment_list}")
    return environment_list

@environment_bp.route('/environment_list',methods=['POST'])
def environment_list():
    #环境列表
    data = request.json
    name = data.get('name')
    environment_name = data.get('environment_name')
    project_id_name = app_base.select_project_id_name(name)  #获取项目的id和名字
    connect = mysql_base.connect_database()
    project_id=project_id_name[0]
    environment_name_id_list=environment_base.environment_list(connect,project_id,environment_name)
    return environment_name_id_list

@environment_bp.route('/environment_add',methods=['POST'])
def environment_add():
    #新增环境
    try:
        data = request.json
        environment_name = data.get('environment_name')
        logging.info(f'environment_name:{environment_name}')
        project_name = data.get('project_name')
        logging.info(f'project_name:{project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        connect = mysql_base.connect_database()
        environment_base.environment_add(connect, name=environment_name, project_id=project_id_name[0])
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增环境成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码


@environment_bp.route('/environment_delete', methods=['POST'])
def environment_delete():
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        environment_name = data.get('environment_name')
        project_name = data.get('project_name')
        logging.info(f'environment_name: {environment_name}, project_name: {project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        logging.info(f'project_id_name: {project_id_name}')
        project_id = project_id_name[0]
        connect = mysql_base.connect_database()
        environment_base.environment_delete(connect, name=environment_name, project_id=project_id)
        mysql_base.disconnect_database(connection=connect)

        success_message = {"message": "删除环境成功"}
        logging.info(f'Success message: {success_message}')
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("删除失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码


@environment_bp.route('/environment_update',methods=['POST'])
def environment_update():
    #修改环境入参：environment_old_name,environment_new_name,project_name,host
    try:
        new_data = request.json
        environment_old_name = new_data.get('environment_old_name')
        logging.info(f'environment_name:{environment_old_name}')
        project_name = new_data.get('project_name')
        logging.info(f'project_name:{project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]  # 获取项目的id
        logging.info(f'project_id:{project_id}')
        connect = mysql_base.connect_database()  # 链接数据库
        environment_name_id = environment_base.environment_id(project_id=project_id,
                                                              environment_name=environment_old_name,
                                                              connection=connect)  # 获取环境名称和id
        logging.info(f'environment_name_id:{environment_name_id}')
        environment_id = environment_name_id[0][1]
        logging.info(f'environment_id:{environment_id}')

        values = (
            new_data.get('environment_new_name'),
            json.dumps(new_data.get('global_variable')),
            json.dumps(new_data.get('debug_global_variable')),
            json.dumps(new_data.get('db')),
            new_data.get('host'),
            json.dumps(new_data.get('headers')),
            new_data.get('global_func'),
            project_id,
            environment_id,
        )
        # 调用函数更新环境配置
        environment_base.environment_update(connect, project_id, environment_id, values)
        mysql_base.disconnect_database(connection=connect)

        success_message = {"message": "修改环境成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("修改失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码


@environment_bp.route('/environment_update1',methods=['POST'])
def environment_update1():
    try:
        new_data = request.json
        environment_old_name = new_data.get('environment_old_name')
        logging.info(f'environment_name:{environment_old_name}')
        project_name = new_data.get('project_name')
        logging.info(f'project_name:{project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]  # 获取项目的id

        connect = mysql_base.connect_database()  # 链接数据库
        environment_name_id = environment_base.environment_id(project_id=project_id, environment_name=environment_old_name,
                                                              connection=connect)  # 获取环境名称和id
        environment_id = environment_name_id[0][1]
        logging.info(f'environment_id:{environment_id}')

        values = (
            new_data.get('environment_new_name'),
            json.dumps(new_data.get('global_variable')),
            json.dumps(new_data.get('debug_global_variable')),
            json.dumps(new_data.get('db')),
            new_data.get('host'),
            json.dumps(new_data.get('headers')),
            new_data.get('global_func'),
            project_id,
            environment_id,
        )

        # new_data = {
        #     'name': '66',
        #     'global_variable': None,
        #     'debug_global_variable': None,
        #     'db':None,
        #     'host': None,
        #     'headers':None,
        #     'global_func': None
        # }
        # project_id = 25
        # environment_id = 4

        # 调用函数更新环境配置
        environment_base.update_environment(connect, project_id, environment_id, values)
        mysql_base.disconnect_database(connection=connect)

        success_message = {"message": "修改环境成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("修改失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码



#
# if __name__=="__main__":
#     environment_add()