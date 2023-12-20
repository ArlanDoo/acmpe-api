from typing import List
from models.event import Event
from datetime import datetime
from utils.event_utils import check_len

import json

class EventStorageException(Exception):
    def __init__(self, message):
        self.message = message
    
    def to_dict(self):
        return {"error": self.message}

class EventEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class EventStorage:
    
    def __init__(self):
        self.counter = 0
        self.storage = {}
        self.last_add_time = datetime.now()
    
    def create(self, event_data: Event) -> dict:
        err_msg = ""
        
        if check_len(event_data.title, 30, False):
            err_msg = "The length of the header should not exceed 30 characters"
            
        elif check_len(event_data.description, 200, False):
            err_msg = "The description must not exceed 200 characters in length"
        
        if not err_msg:
            self.counter += 1
            event_data.id = str(self.counter)
            self.storage[event_data.id] = event_data
            
            return {
                "result": json.loads(
                    json.dumps(event_data, cls=EventEncoder)
                )
            }
        else:
            error = EventStorageException(err_msg)
            return error.to_dict()
    
    def read(self, _id_: int) -> dict:
        if _id_ in self.storage:
            return {
                "result": json.loads(
                    json.dumps(self.storage[_id_], cls=EventEncoder)
                )
            }
        return {
            "result": f"Event {_id_} is not found"
        }
    
    def list(self) -> List:
        return {
            "result": json.loads(
                json.dumps(list(self.storage.values()), cls=EventEncoder)
            )
        }
    
    def update(self, _id_: int, event_data: dict) -> dict:
        if _id_ in self.storage:
            self.storage[_id_].title = event_data["title"]
            self.storage[_id_].date = event_data["date"]
            self.storage[_id_].description = event_data["description"]
            
            return {
                "result": json.loads(
                    json.dumps(self.storage[_id_], cls=EventEncoder)
                )
            }
        return {
            "result": f"Event {_id_} is not found"
        }
        
    def delete(self, _id_: int) -> dict:
        if _id_ in self.storage:
            del self.storage[_id_]
            
            return {
                "result": f"Event number {_id_} has been deleted"
            }
        return {
            "result": f"Event {_id_} is not found"
        }