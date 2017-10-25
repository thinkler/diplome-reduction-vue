from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
from lib import core
import pdb
import csv
import io
import numpy as np
from werkzeug.datastructures import ImmutableMultiDict
import base64

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@cross_origin()
@app.route('/reduction', methods=['POST'])
def upload_data():
    table = request.get_json()['table']
    factors = int(request.get_json()['factors'])
    return jsonify(core.reduct(table, factors))

# Get Method
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Get Method with ID
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# Post Method
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)
