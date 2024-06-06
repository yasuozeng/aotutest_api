import logging
from flask import Flask, jsonify, request, Blueprint
from base import mysql_base, report_base
import json

app = Flask(__name__)
report_bp = Blueprint('report', __name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@report_bp.route('/report_add', methods=['POST'])
def report_add():
    # 新增 report
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        info = data.get('info').encode('utf-8')  # 将 info 转换为二进制数据
        values = (
            info,
            data.get('record'),
            data.get('testtask_id')
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        report_base.report_add(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "新增 report 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error(f"新增 report 失败，错误信息: {e}")
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@report_bp.route('/report_delete', methods=['POST'])
def report_delete():
    # 删除 report
    try:
        data = request.json
        report_id = data.get('id')
        logging.info(f'report_id: {report_id}')
        connect = mysql_base.connect_database()
        report_base.report_delete(connect, report_id)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "删除 report 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error(f"删除 report 失败，错误信息: {e}")
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@report_bp.route('/report_list', methods=['POST'])
def report_list():
    # 查询 report 列表
    try:
        connect = mysql_base.connect_database()
        report_list = report_base.report_list(connect)
        mysql_base.disconnect_database(connection=connect)
        return jsonify(report_list), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error(f"查询 report 列表失败，错误信息: {e}")
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

@report_bp.route('/report_update', methods=['POST'])
def report_update():
    # 修改 report
    try:
        data = request.json
        logging.info(f'Received data: {data}')
        report_id = data.get('id')
        info = data.get('info').encode('utf-8')  # 将 info 转换为二进制数据
        values = (
            info,
            data.get('record'),
            data.get('testtask_id'),
            report_id
        )
        logging.info(f'values: {values}')
        connect = mysql_base.connect_database()
        report_base.report_update(connect, values)
        mysql_base.disconnect_database(connection=connect)
        success_message = {"message": "修改 report 成功"}
        return jsonify(success_message), 200  # 返回JSON响应和HTTP状态码
    except Exception as e:
        logging.error(f"修改 report 失败，错误信息: {e}")
        return jsonify({"error": str(e)}), 500  # 返回错误信息和HTTP状态码

if __name__ == '__main__':

    app.run(debug=True)
