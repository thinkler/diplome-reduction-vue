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
    return jsonify(core.reduct(table))

@app.route('/method', methods=['POST'])
def reduct_data():
    table = request.get_json()['table']
    r_method = request.get_json()['method']
    factors = int(request.get_json()['factors'])
    return jsonify(core.method(table, r_method, factors))
