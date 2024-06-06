import requests
import json
base_url = "http://localhost:5000"

def project_list():

    url = "http://localhost:5000/project/project_list"  # 确保这与运行Flask应用的地址和端口匹配

    response = requests.get(url)
    print(response.json())
    print(type(response.json()))
    if response.status_code == 200:
        print("Unique first elements:", response.json())
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")

def project_add():

    # 定义接口URL，确保与实际部署的地址一致
    url = "http://localhost:5000/project/project_add"
    # 准备要发送的JSON数据
    data = {
        "name": "自动化测试平台"
    }
    # 发送POST请求
    response = requests.post(url, json=data)

    # 检查响应状态码
    if response.status_code == 200:
        # 处理成功的响应
        result = response.text
        print(result)  # 输出服务器返回的信息，例如："新建项目成功" 或 "新建项目失败"
    else:
        # 处理错误情况
        print(f"请求失败，状态码：{response.status_code}")


def project_delete():

    # 定义接口URL，确保与实际部署的地址一致
    url = "http://localhost:5000/project/project_delete"

    # 准备要发送的JSON数据
    data = {
        "name": "项目1"
    }

    # 发送POST请求
    response = requests.post(url, json=data)

    # 检查响应状态码
    if response.status_code == 200:
        # 处理成功的响应
        result = response.text
        print(result)  # 输出服务器返回的信息，例如："新建项目成功" 或 "新建项目失败"
    else:
        # 处理错误情况
        print(f"请求失败，状态码：{response.status_code}")

def environment_name_list():

    url = "http://localhost:5000/environment/environment_name_list"  # 替换为实际的服务器地址
    data = {
        "name": "百度"  # 替换为实际的项目名称
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        environment_list = response.json()
        print("Environment List:", environment_list)
    else:
        print("Failed to fetch environment list:", response.status_code, response.text)


def environment_list():

    url = "http://localhost:5000/environment/environment_list"  # 替换为实际的服务器地址
    data = {
        "name": "百度"  # 替换为实际的项目名称
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        environment_list = response.json()
        print("Environment List:", environment_list)
    else:
        print("Failed to fetch environment list:", response.status_code, response.text)

def environment_add():
    url = "http://localhost:5000/environment/environment_add"  # 替换为实际的服务器地址
    data = {
        "project_name": "自动化测试平台",  # 替换为实际的环境名称
        "environment_name":"自动化测试平台环境"
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Environment added successfully.")
    else:
        print("Failed to add environment:", response.status_code, response.text)

def environment_delete():
    url = "http://localhost:5000/environment/environment_delete"  # 替换为实际的服务器地址
    data = {
        "project_name": "004",  # 替换为实际的环境名称
        "environment_name":"44"
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Environment added successfully.")
    else:
        print("Failed to add environment:", response.status_code, response.text)

def environment_update():
    url = 'http://localhost:5000/environment/environment_update'  # 修改为你的服务器地址

    data = {
        # 'environment_old_name': '77',
        # 'environment_new_name': '123',
        'environment_old_name': '自动化测试平台环境',
        'environment_new_name': '自动化测试平台环境',
        'project_name': '自动化测试平台',
        'host': 'http://localhost:5000',
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("环境修改成功")
    else:
        print("环境修改失败:", response.json())

def interface_add():
    # 新增接口
    headers = {
        "Content-Type": "application/json",  # 设置正确的Content-Type
    }
    add_data = {
        "project_name": "自动化测试平台",
        "name": "2自动化测试平台项目新增接口",
        "url": "/project/2project_add",
        "method": "POST",
        "type": "1"
    }
    response = requests.post(f"http://localhost:5000/interface/interface_add", json=add_data,headers=headers)
    print(response.text)

def interface_delete():
    # 删除接口
    delete_data = {
        "project_name": "003",
        "name": "24接口24"
    }
    response = requests.post(f"http://localhost:5000/interface/interface_delete", json=delete_data)
    print(response.text)

def interface_detaila():
    # 删除接口
    delete_data = {
        "project_name": "004",
        "name": "啊"
    }
    response = requests.post(f"http://localhost:5000/interface/interface_details", json=delete_data)
    response_json=response.json()
    print(response_json)

def interface_list():
    # 查询接口列表
    headers = {
        "Content-Type": "application/json",  # 设置正确的Content-Type
    }
    list_data = {
        "project_name": "自动化测试平台"
        # "project_name": "004"
    }
    response = requests.post("http://localhost:5000/interface/interface_list", json=list_data,headers=headers)
    # 确保响应内容为 UTF-8 编码
    # response.encoding = 'utf-8'
    response_text=response.text
    response_json = response.json()
    print(response_json)
    extracted_values = [entry for entry in response_json ]
    interface_name_list = []
    for entry_list in response_json:
        i = 0
        print(f'entry_list:{entry_list}')
        for entry in entry_list:
            i=i+1
            if i==3:
                print(f'entry:{entry}')
                interface_name_list.append(entry)

    print(interface_name_list)


def interface_update():
    # 修改接口
    update_data = {
        "project_name": "自动化测试平台",
        "name": "Updated Interface",
        "url": "/api/updated",
        "method": "POST",
        "type": "2",
        "interface_old_name": '11'  # 假设这是要修改的接口ID
    }
    response = requests.post(f"http://localhost:5000/interface/interface_update", json=update_data)
    print(response.text)


BASE_URL = "http://127.0.0.1:5000/intercase"

# Function to add an InterCase
def add_intercase():
    url = f"{BASE_URL}/intercase_add"
    # data = {
    #     "project_name": "自动化测试平台",
    #     "title": "1testaa",
    #     'interface_id':2,
    #     "headers": {"Content-Type": "application/json"},
    #     "request": {"key": "value"},
    #     "file": {"file_key": "file_value"},
    #     "setup_script": "setup_script_content",
    #     "teardown_script": "teardown_script_content"
    # }

    data = {
        "project_name": "自动化测试平台",
        "title": "2testaa",
        # 'interface_id':2,
        # "headers": {"Content-Type": "application/json"},
        # "request": {"key": "value"},
        # "file": {"file_key": "file_value"},
        # "setup_script": "setup_script_content",
        # "teardown_script": "teardown_script_content"
    }

    response = requests.post(url, json=data)
    return response.json()

# Function to list all InterCases for a project
def list_intercase():
    url = f"{BASE_URL}/intercase_list"
    data = {"project_name": "自动化测试平台"}
    response = requests.post(url, json=data)
    print(response.text)
    return response.json()

# Function to update an InterCase
def update_intercase():
    url = f"{BASE_URL}/intercase_update"
    data = {
        "project_name": "自动化测试平台",
        'interface_id': 2,
        "old_title": "new_title",
        "headers": {"Content-Type": "application/json"},
        "request": {"name": "1test项目新增"},
        "file": {"": ""},
        "setup_script": "",
        "teardown_script": "",
        "new_title": "1"
    }
    response = requests.post(url, json=data)
    return response.json()

# Function to delete an InterCase
def delete_intercase(intercase_name):
    url = f"{BASE_URL}/intercase_delete"
    data = {"id": intercase_name}
    response = requests.post(url, json=data)
    return response.json()


def add_scene():
    url = f"{base_url}/scene/scene_add"
    data = {
        "project_name": "自动化测试平台",
        "name": "12"
    }
    response = requests.post(url, json=data)
    return response.json()

# Function to list all scenes for a project
def list_scene():
    url = f"{base_url}/scene/scene_list"
    data = {"project_name": "自动化测试平台"}
    response = requests.post(url, json=data)
    print(response.text)
    return response.text

# Function to update a scene
def update_scene():
    url = f"{base_url}/scene/scene_update"
    data = {
        "old_name": '21',
        "project_name": "自动化测试平台",
        "new_name": "66"
    }
    response = requests.post(url, json=data)
    return response.json()

# Function to delete a scene
def delete_scene(scene_name):
    url = f"{base_url}/scene/scene_delete"
    data = {"scene_name": scene_name}
    response = requests.post(url, json=data)
    return response.json()

def add_scenetocase():
    url = "http://127.0.0.1:5000/scenetocase/scenetocase_add"
    data = {
        "case_name": '1testaa',
        "scene_name": 'New Scene',
        "sort": 2
    }
    response = requests.post(url, json=data)
    return response.json()

# Function to list all SceneToCase for a scene
def list_scenetocase(scene_name):
    url = "http://127.0.0.1:5000/scenetocase/scenetocase_list"
    data = {"scene_name": scene_name}
    response = requests.post(url, json=data)
    print(response.text)
    return response.json()

# Function to update a SceneToCase
def update_scenetocase(scenetocase_name):
    url = "http://127.0.0.1:5000/scenetocase/scenetocase_update"
    data = {
        "id": scenetocase_name,
        "case_name": 66,
        "scene_name": 66,
        "sort": 66
    }
    response = requests.post(url, json=data)
    print(response.text)
    return response.json()

# Function to delete a SceneToCase
def delete_scenetocase(scenetocase_name):
    url = "http://127.0.0.1:5000/scenetocase/scenetocase_delete"
    data = {"id": scenetocase_name}
    response = requests.post(url, json=data)
    return response.json()

def add_testtask():
    url = f"http://127.0.0.1:5000/testtask/testtask_add"
    data = {
        "project_id": 29,
        "name_id": 2,
        "scent_id": 1
    }
    response = requests.post(url, json=data)
    print(response.json())

def delete_testtask(testtask_id):
    url = f"http://127.0.0.1:5000/testtask/testtask_delete"
    data = {"id": testtask_id}
    response = requests.post(url, json=data)
    print(response.json())

def list_testtasks(project_id):
    url = f"http://127.0.0.1:5000/testtask/testtask_list"
    data = {"project_id": project_id}
    response = requests.post(url, json=data)
    print(response.json())

def update_testtask(testtask_id):
    url = f"http://127.0.0.1:5000/testtask/testtask_update"
    data = {
        "id": testtask_id,
        "project_id": 29,
        "name_id": 3,
        "scent_id": 2
    }
    response = requests.post(url, json=data)
    print(response.json())


def add_testreport():
    url = f"http://127.0.0.1:5000/testreport/testreport_add"
    data = {
        "info": "<html><body><h1>Test Report</h1></body></html>",
        "record": 1,
        "testtask_id": 1
    }
    response = requests.post(url, json=data)
    print(response.json())

def delete_testreport(testreport_id):
    url = f"http://127.0.0.1:5000/testreport/testreport_delete"
    data = {"id": testreport_id}
    response = requests.post(url, json=data)
    print(response.json())

def list_testreport():
    url = f"http://127.0.0.1:5000/testreport/testreport_list"
    response = requests.post(url)
    print(response.json())

def update_testreport(testreport_id):
    url = f"http://127.0.0.1:5000/testreport/testreport_update"
    data = {
        "id": testreport_id,
        "info": "<html><body><h1>Updated Test Report</h1></body></html>",
        "record": 1,
        "testtask_id": 1
    }
    response = requests.post(url, json=data)
    print(response.json())


if __name__ == "__main__":
    # project_list()
    # project_add()
    # project_list()
    # project_delete()
    # project_list()

    # environment_list()
    # environment_name_list()
    # environment_add()
    # environment_list()
    # environment_delete()
    # environment_list()
    # environment_update()

    # interface_list()
    # interface_detaila()
    # interface_add()
    # interface_delete()
    # interface_update()

    # delete_intercase(intercase_name=4)
    # list_intercase()
    # update_intercase()
    # add_intercase()
    # list_intercase()
    # update_intercase()

    # add_scene()
    update_scene()
    # delete_scene(scene_name='12')
    # list_scene()

    # add_scenetocase()
    # list_scenetocase(2)
    # update_scenetocase(3)
    # delete_scenetocase(3)






