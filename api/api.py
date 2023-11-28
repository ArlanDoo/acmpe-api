from flask import Flask, jsonify, request, render_template
from config.config import MAIN_PATH_API
from models.event import Event
from utils.db import EventDB

app = Flask(__name__)
event_storage = EventDB()

@app.route(f"{MAIN_PATH_API}/event/create/", methods = ["POST"])
def create():
    create_data = request.get_json()
    event = Event(create_data["id"],
                  create_data["date"],
                  create_data["title"],
                  create_data["description"])
    
    return str(event_storage.create(event))

@app.route(f"{MAIN_PATH_API}/event/list/", methods = ["GET"])
def list():
    return "list"

@app.route(f"{MAIN_PATH_API}/event/read/<_id_>/", methods = ["GET"])
def read(_id_):
    return event_storage.read(_id_)

@app.route(f"{MAIN_PATH_API}/event/update/<_id_>/", methods = ["PUT"])
def update(_id_):
    return f"update {_id_}"

@app.route(f"{MAIN_PATH_API}/event/delete/<_id_>/", methods = ["DELETE"])
def delete(_id_):
    return f"delete {_id_}"