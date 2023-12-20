from flask import Flask,request, jsonify
from config.config import MAIN_PATH_API
from interfaces.db_event import EventsStorageDB

from models.event import Event

app = Flask(__name__)
MAIN_PATH = MAIN_PATH_API
eventstorage = EventsStorageDB()

@app.route(f"{MAIN_PATH}/event/", methods=["GET"])
def ping_api():
    return jsonify({
        "ping": "The resource is available"
    }), 200

@app.route(f"{MAIN_PATH}/event/add_event/", methods=["POST"])
def create_event():
    
    req_data = request.get_json()
    event = Event(0,
                  req_data["date"],
                  req_data["title"],
                  req_data["description"]
                  )
    
    return jsonify(eventstorage.create(event)), 201

@app.route(f"{MAIN_PATH}/event/list/", methods=["GET"])
def list_event():

    return jsonify(eventstorage.list()), 200

@app.route(f"{MAIN_PATH}/event/get_event/<_id_>/", methods=["GET"])
def read_event(_id_):
    
    return jsonify(eventstorage.read(_id_)), 200

@app.route(f"{MAIN_PATH}/event/update_event/<_id_>/", methods=["PUT"])
def update_event(_id_):
    
    req_data = request.get_json()
    return jsonify(eventstorage.update(_id_, req_data)), 200

@app.route(f"{MAIN_PATH}/event/delete_event/<_id_>/", methods=["DELETE"])
def delete_event(_id_):
    
    return jsonify(eventstorage.delete(_id_)), 200