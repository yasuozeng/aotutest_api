import logging
from flask import Flask, jsonify, request,Blueprint, jsonify
from base import mysql_base,app_base,project_base,environment_base,interface_base
from flask import json


interface_bp=Blueprint('interface',__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@interface_bp.route('/interface_add',methods=['POST'])
def interface_add():
    #新增接口
    try:
        data = request.json
        project_name = data.get('project_name')
        logging.info(f'project_name:{project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        logging.info(f'project_id_name:{project_id_name}')
        values = (
            project_id_name[0],
            data.get('name'),
            data.get('url'),
            data.get('method'),
            data.get('type'),
        )
        logging.info(f'values:{values}')
        connect = mysql_base.connect_database()
        interface_base.interface_add(connect,values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增接口成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@interface_bp.route('/interface_delete',methods=['POST'])
def interface_delete():
    #删除接口
    try:
        data = request.json
        project_name = data.get('project_name')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        values = (
            project_id_name[0],
            data.get('name'),
        )
        logging.info(f'values:{values}')
        connect = mysql_base.connect_database()
        interface_base.interface_delete(connect,values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "删除接口成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("删除接口失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@interface_bp.route('/interface_list',methods=['POST'])
def interface_list():
    #查询接口
    try:
        data = request.json
        project_name = data.get('project_name')
        logging.info(f'project_name:{project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        logging.info(f'project_id_name:{project_id_name}')
        project_id = project_id_name[0]
        logging.info(f'project_id:{project_id}')
        connect = mysql_base.connect_database()
        interface_list=interface_base.interface_list(connect, project_id)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "查询接口成功"}
        return interface_list  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询接口失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码


@interface_bp.route('/interface_update',methods=['POST'])
def interface_update():
    #修改接口
    try:
        new_data = request.json
        project_name=new_data.get('project_name')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]  # 获取项目的id
        logging.info(f'project_id:{project_id}')
        connect = mysql_base.connect_database()  # 链接数据库

        values = (
            new_data.get('name'),
            new_data.get('url'),
            new_data.get('method'),
            new_data.get('type'),
            project_id,
            new_data.get('interface_old_name')
        )
        interface_base.interface_update(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "修改接口成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("接口修改失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@interface_bp.route('/interface_details',methods=['POST'])
def interface_details():
    #查看接口
    try:
        data = request.json
        project_name = data.get('project_name')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        values = (
            project_id_name[0],
            data.get('name'),
        )
        logging.info(f'values:{values}')
        connect = mysql_base.connect_database()
        interface_details = interface_base.interface_details(connect,values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "查看接口成功"}
        return jsonify(interface_details), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查看接口失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码