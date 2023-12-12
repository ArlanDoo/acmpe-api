from typing import List
from models.event import Event
from utils.valid_utils import len_more_then
from datetime import datetime

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
        self._storage = {}
        self.l_time_add = datetime.now()
    
    def create(self, event: Event) -> str:
        if len_more_then(event.title, 30):
            error = EventStorageException(f"Title length more then 30 symbol")
            return error.to_dict()
        
        elif len_more_then(event.description, 200):
            error = EventStorageException(f"Description length more then 200 symbol")
            return error.to_dict()
        
        else:
            self.counter += 1
            event.id = str(self.counter)
            self._storage[event.id] = event
            
            return {"result": f"Event {event.id} created"}
    
    def read(self, _id: str) -> Event:
        if not _id:
            error = EventStorageException(f"Event number not found")
            return error.to_dict() 
        elif _id not in self._storage:
            error = EventStorageException(f"Event {_id} not found")
            return error.to_dict()
        
        # return {"response":
        #             {
        #                 "id": self._storage[_id].id,
        #                 "title": self._storage[_id].title,
        #                 "date": self._storage[_id].date,
        #                 "description": self._storage[_id].description
        #             }
        #         }
        return {"event": json.dumps(self._storage[_id], cls=EventEncoder)}
    
    def list(self) -> List[Event]:
        # return json.dumps(list(self._storage.values()))
        if not len(self._storage):
            error = EventStorageException(f"Events not found")
            return error.to_dict()
        return {
            "list": json.dumps(list(self._storage.values()), cls=EventEncoder)
        }
    
    def update(self, _id: str, event: Event) -> Event:
        if _id not in self._storage:
            error = EventStorageException(f"Event {_id} is not found")
            return error.to_dict()
        else:
            self._storage[_id] = event
            return {
                "update": f"Event {_id} is update"
            }
    
    def delete(self, _id: str) -> Event:
        if _id not in self._storage:
            error = EventStorageException(f"Event {_id} is not found")
            return error.to_dict()
        
        else:
            del self._storage[_id]
            return {
                "delete": f"Event {_id} is deleted"
            }