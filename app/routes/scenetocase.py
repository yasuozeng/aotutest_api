import logging
from flask import Flask, jsonify, request, Blueprint
from base import mysql_base, app_base, scenetocase_base
import json

app = Flask(__name__)
scenetocase_bp = Blueprint('scenetocase', __name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@scenetocase_bp.route('/scenetocase_add', methods=['POST'])
def scenetocase_add():
    # 新增 SceneToCase
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        values = (
            data.get('case_name'),
            data.get('scene_name'),
            data.get('sort')
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        scenetocase_base.scenetocase_add(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增 SceneToCase 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("新增 SceneToCase 失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@scenetocase_bp.route('/scenetocase_delete', methods=['POST'])
def scenetocase_delete():
    # 删除 SceneToCase
    try:
        data = request.json
        scenetocase_name = data.get('id')
        logging.info(f'scenetocase_name: {scenetocase_name}')
        connect = mysql_base.connect_database()
        scenetocase_base.scenetocase_delete(connect, scenetocase_name)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "删除 SceneToCase 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("删除 SceneToCase 失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@scenetocase_bp.route('/scenetocase_list', methods=['POST'])
def scenetocase_list():
    # 查询 SceneToCase 列表
    try:
        data = request.json
        scene_name = data.get('scene_name')
        logging.info(f'scene_name: {scene_name}')
        connect = mysql_base.connect_database()
        scenetocase_list = scenetocase_base.scenetocase_list(connect, scene_name)
        mysql_base.disconnect_database(connection=connect)
        return jsonify(scenetocase_list), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("查询 SceneToCase 列表失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@scenetocase_bp.route('/scenetocase_update', methods=['POST'])
def scenetocase_update():
    # 修改 SceneToCase
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        scenetocase_name = data.get('id')
        values = (
            data.get('case_name'),
            data.get('scene_name'),
            data.get('sort'),
            scenetocase_name
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        scenetocase_base.scenetocase_update(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "修改 SceneToCase 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error("修改 SceneToCase 失败，错误信息: %s", e)
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码




