from flask import Flask, jsonify, request
from config.config import MAIN_PATH_API
from models.event import Event
from utils.db import EventDB

import json

app = Flask(__name__)
event_storage = EventDB()

@app.route(f"{MAIN_PATH_API}/event/create/", methods = ["POST"])
def create():
    try:
        create_data = request.get_json()
        event = Event(0,
                    create_data["date"],
                    create_data["title"],
                    create_data["description"]
                )
        return jsonify(event_storage.create(event)), 201
    
    except Exception as ex:
        return jsonify({
            "error": f"Excpt: {ex}. Failed create note"
        }), 404

@app.route(f"{MAIN_PATH_API}/event/read/<_id_>/", methods = ["GET"])
def read(_id_):
    try:
        return jsonify(event_storage.read(_id_)), 200
    
    except Exception as ex:
        return jsonify({
            "error": f"Excpt: {ex}. Failed read note"
        }), 404

@app.route(f"{MAIN_PATH_API}/event/list/", methods = ["GET"])
def list():
    try:
        return jsonify(event_storage.list())
    
    except Exception as ex:
        return jsonify({
            "error": f"Excpt: {ex}. Failed list note"
        }), 404

@app.route(f"{MAIN_PATH_API}/event/update/<_id_>/", methods = ["PUT"])
def update(_id_):
    try:
        create_data = request.get_json()
        event = Event(str(_id_),
                    create_data["date"],
                    create_data["title"],
                    create_data["description"])
        
        return jsonify(event_storage.update(_id_, event))

    except Exception as ex:
        return jsonify({
            "error": f"Excpt: {ex}. Failed update note"
        }), 404

@app.route(f"{MAIN_PATH_API}/event/delete/<_id_>/", methods = ["DELETE"])
def delete(_id_):
    try:
        return jsonify(event_storage.delete(_id_))
        
    except Exception as ex:
        return jsonify({
            "error": f"Excpt: {ex}. Failed delete note"
        }), 404