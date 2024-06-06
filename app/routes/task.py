import logging
from flask import Flask, jsonify, request, Blueprint
from base import mysql_base, app_base, task_base
import json

app = Flask(__name__)
task_bp = Blueprint('task', __name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@task_bp.route('/task_add', methods=['POST'])
def task_add():
    # 新增 task
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        values = (
            data.get('project_id'),
            data.get('name'),
            data.get('scenet_id')
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        task_base.task_add(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增 task 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("新增 task 失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@task_bp.route('/task_delete', methods=['POST'])
def task_delete():
    # 删除 task
    try:
        data = request.json
        task_id = data.get('id')
        logging.info(f'task_id: {task_id}')
        connect = mysql_base.connect_database()
        task_base.task_delete(connect, task_id)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "删除 task 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("删除 task 失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@task_bp.route('/task_list', methods=['POST'])
def task_list():
    # 查询 task 列表
    try:
        data = request.json
        project_id = data.get('project_id')
        logging.info(f'project_id: {project_id}')
        connect = mysql_base.connect_database()
        task_list = task_base.task_list(connect, project_id)
        mysql_base.disconnect_database(connection=connect)
        return jsonify(task_list), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询 task 列表失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@task_bp.route('/task_update', methods=['POST'])
def task_update():
    # 修改 task
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        task_id = data.get('id')
        values = (
            data.get('project_id'),
            data.get('name'),
            data.get('scenet_id'),
            task_id
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        task_base.task_update(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "修改 task 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("修改 task 失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码






