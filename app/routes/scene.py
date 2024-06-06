import logging
from flask import Flask, jsonify, request, Blueprint
from base import mysql_base, app_base, scene_base
import json

app = Flask(__name__)
scene_bp = Blueprint('scene', __name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@scene_bp.route('/scene_add', methods=['POST'])
def scene_add():
    # 新增 scene
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        project_name = data.get('project_name')
        logging.info(f'project_name: {project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]
        values = (
            project_name,
            data.get('name')
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        scene_base.scene_add(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增场景成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("新增场景失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@scene_bp.route('/scene_delete', methods=['POST'])
def scene_delete():
    # 删除 scene
    try:
        data = request.json
        scene_name = data.get('scene_name')
        logging.info(f'scene_name: {scene_name}')
        connect = mysql_base.connect_database()
        scene_base.scene_delete(connect, scene_name)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "删除场景成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("删除场景失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@scene_bp.route('/scene_list', methods=['POST'])
def scene_list():
    # 查询 scene 列表
    try:
        data = request.json
        project_name = data.get('project_name')
        logging.info(f'project_name: {project_name}')
        project_id_name = app_base.select_project_id_name(project_name)  # 获取项目的id和名字
        project_id = project_id_name[0]
        logging.info(f'project_id: {project_id}')
        connect = mysql_base.connect_database()
        scene_list = scene_base.scene_list(connect, project_name)
        mysql_base.disconnect_database(connection=connect)
        return jsonify(scene_list), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询场景列表失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@scene_bp.route('/scene_update', methods=['POST'])
def scene_update():
    # 修改 scene
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        scene_id = data.get('id')
        values = (
            data.get('new_name'),
            data.get('old_name'),
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        scene_base.scene_update(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "修改场景成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("修改场景失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码


