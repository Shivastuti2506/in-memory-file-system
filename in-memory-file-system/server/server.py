from flask import Flask, request, jsonify
import os
import shutil

project_app = Flask(__name__)

# In-memory file system structure
filesystem = {'/': {}}
current_directory = '/'


def get_abs_path(path):
    if not path.startswith('/'):
        path = os.path.join(current_directory, path)
    
    # Ensure the path is normalized to handle directories correctly
    path = os.path.normpath(path)
    
    return path

@project_app.route('/mkdir', methods=['POST'])
def mkdir():
    data = request.get_json()
    dir_name = data.get('directory_name')

    if not dir_name:
        return jsonify({"error": "Directory name not provided"}), 400

    abs_path = get_abs_path(dir_name)
    if abs_path in filesystem:
        return jsonify({"error": "Directory already exists"}), 400

    filesystem[abs_path] = {}
    return jsonify({"message": f"Directory '{abs_path}' created successfully"}), 200

@project_app.route('/ls', methods=['GET'])
def ls():
    data = request.args
    dir_name = data.get('dir_name', '.')

    abs_path = get_abs_path(dir_name)
    if abs_path not in filesystem:
        return jsonify({"error": f"Directory '{abs_path}' not found"}), 404

    contents = list(filesystem[abs_path].keys())
    return jsonify({"contents": contents}), 200

@project_app.route('/cd', methods=['POST'])
def cd():
    data = request.get_json()
    dir_name = data.get('dir_name', '/')

    abs_path = get_abs_path(dir_name)
    if abs_path not in filesystem:
        return jsonify({"error": f"Directory '{abs_path}' not found"}), 404

    global current_directory
    current_directory = abs_path
    return jsonify({"message": f"Current directory changed to '{current_directory}'"}), 200

@project_app.route('/mv', methods=['POST'])
def mv():
    data = request.get_json()
    src = data.get('source')
    dest = data.get('destination')

    source_abs_path = get_abs_path(src)
    destination_abs_path = get_abs_path(dest)

    if source_abs_path not in filesystem:
        return jsonify({"error": f"Source '{source_abs_path}' not found"}), 404

    if destination_abs_path in filesystem:
        return jsonify({"error": f"Destination '{destination_abs_path}' already exists"}), 400

    filesystem[destination_abs_path] = filesystem.pop(source_abs_path)
    return jsonify({"message": f"Moved '{source_abs_path}' to '{destination_abs_path}'"}), 200

@project_app.route('/cp', methods=['POST'])
def cp():
    data = request.get_json()
    source = data.get('source')
    destination = data.get('destination')

    source_abs_path = get_abs_path(source)
    destination_abs_path = get_abs_path(destination)

    if source_abs_path not in filesystem:
        return jsonify({"error": f"Source '{source_abs_path}' not found"}), 404

    if destination_abs_path in filesystem:
        return jsonify({"error": f"Destination '{destination_abs_path}' already exists"}), 400

    shutil.copytree(source_abs_path, destination_abs_path)
    return jsonify({"message": f"Copied '{source_abs_path}' to '{destination_abs_path}'"}), 200

@project_app.route('/rm', methods=['POST'])
def rm():
    data = request.get_json()
    target = data.get('target')

    target_abs_path = get_abs_path(target)

    if target_abs_path not in filesystem:
        return jsonify({"error": f"Target '{target_abs_path}' not found"}), 404

    if target_abs_path == '/':
        return jsonify({"error": "Cannot remove the root directory"}), 400

    filesystem.pop(target_abs_path, None)
    return jsonify({"message": f"Removed '{target_abs_path}'"}), 200

# New Routes for cat, touch, and echo

@project_app.route('/cat', methods=['GET'])
def cat():
    data = request.args
    file_path = data.get('file_path')

    abs_path = get_abs_path(file_path)
    if abs_path not in filesystem or not os.path.isfile(abs_path):
        return jsonify({"error": f"File '{abs_path}' not found"}), 404

    with open(abs_path, 'r') as file:
        content = file.read()

    return jsonify({"content": content}), 200

@project_app.route('/touch', methods=['POST'])
def touch():
    data = request.get_json()
    file_path = data.get('file_path')

    abs_path = get_abs_path(file_path)
    if abs_path in filesystem:
        return jsonify({"error": f"File '{abs_path}' already exists"}), 400

    open(abs_path, 'w').close()
    return jsonify({"message": f"File '{abs_path}' created successfully"}), 200

@project_app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    file_path = data.get('file_path')
    content = data.get('content')

    abs_path = get_abs_path(file_path)
    if abs_path not in filesystem or not os.path.isfile(abs_path):
        return jsonify({"error": f"File '{abs_path}' not found"}), 404

    with open(abs_path, 'w') as file:
        file.write(content)

    return jsonify({"message": f"Content written to '{abs_path}'"}), 200

@project_app.route('/grep', methods=['GET'])
def grep():
    data = request.args
    file_path = data.get('file_path')
    pattern = data.get('pattern')

    abs_path = get_abs_path(file_path)
    if abs_path not in filesystem or not os.path.isfile(abs_path):
        return jsonify({"error": f"File '{abs_path}' not found"}), 404

    with open(abs_path, 'r') as file:
        lines = file.readlines()

    matching_lines = [line.strip() for line in lines if pattern in line]

    return jsonify({"matching_lines": matching_lines}), 200

if __name__ == '__main__':
    project_app.run(debug=True)
