import logging
from flask import Flask, jsonify, request, Blueprint
from base import mysql_base, app_base, intercase_base
import json

app = Flask(__name__)
intercase_bp = Blueprint('intercase', __name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@intercase_bp.route('/intercase_add', methods=['POST'])
def intercase_add():
    # 新增 InterCase
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        project_name = data.get('project_name')
        logging.info(f'project_name: {project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]
        values = (
            data.get('project_name'),
            data.get('title'),
            data.get('interface_id', ),
            json.dumps(data.get('headers', {})),
            json.dumps(data.get('request', {})),
            json.dumps(data.get('file', {})),
            data.get('setup_script', ''),
            data.get('teardown_script', '')
        )

        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        intercase_base.intercase_add(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增用例成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("新增用例失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@intercase_bp.route('/intercase_delete', methods=['POST'])
def intercase_delete():
    # 删除 InterCase
    try:
        data = request.json
        intercase_id = data.get('title')
        logging.info(f'intercase_id: {intercase_id}')
        connect = mysql_base.connect_database()
        intercase_base.intercase_delete(connect, intercase_id)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "删除用例成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("删除用例失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@intercase_bp.route('/intercase_list', methods=['POST'])
def intercase_list():
    # 查询 InterCase
    try:
        data = request.json
        project_name = data.get('project_name')
        logging.info(f'project_name: {project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]
        logging.info(f'project_id: {project_id}')
        connect = mysql_base.connect_database()
        intercase_list = intercase_base.intercase_list(connect, project_name)
        mysql_base.disconnect_database(connection=connect)
        return jsonify(intercase_list), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询用例失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码


@intercase_bp.route('/intercase_update', methods=['POST'])
def intercase_update():
    try:
        data = request.json
        logging.info(f'Received data: {data}')

        values = (
            data.get('project_name'),
            data.get('new_title'),
            data.get('interface_id'),
            json.dumps(data.get('headers')),
            json.dumps(data.get('request')),
            json.dumps(data.get('file')),
            data.get('setup_script'),
            data.get('teardown_script'),
            data.get('old_title')
        )

        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        intercase_base.intercase_update(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "修改用例成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("修改用例失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@intercase_bp.route('/intercase_details', methods=['POST'])
def intercase_details():
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        values = (
            data.get('project_name'),
            data.get('old_title')
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        detaile_list =  intercase_base.intercase_details(connect, values)
        mysql_base.disconnect_database(connection=connect)
        return jsonify(detaile_list), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("新增用例失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码



