from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from producer import produce_message
from db import insert_db
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/produce", methods=['POST'])
def send_data():
    body = request.get_json()
    produce_message(body)
    return jsonify({"success": True })

@app.route("/insert", methods=['POST'])
def insert_product():
    body = request.get_json()
    result = insert_db(body)
    return jsonify({"success": True, "response": {"id": result[0]}})


    
