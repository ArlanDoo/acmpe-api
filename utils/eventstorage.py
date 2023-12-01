from typing import List
from models.event import Event
from utils.valid_utils import len_more_then

class EventStorageException(Exception):
    def __init__(self, message):
        self.message = message
    
    def to_dict(self):
        return {"Error": self.message}

class EventStorage:
    def __init__(self):
        self.counter = 0
        self._storage = {}
    
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
            
            return {"response": f"Event {event.id} created"}
    
    def read(self, _id: str) -> Event:
        if _id not in self._storage:
            error = EventStorageException(f"Event {_id} is not found")
            return error.to_dict()
        return {"response": dict(self._storage[_id])}
    
    def list(self) -> List[Event]:
        return list(self._storage.values())
    
    def update(self, _id: str, event: Event) -> Event:
        if _id not in self._storage:
            return EventStorageException(f"Event {_id} is not found")
        else:
            self._storage[_id] = event
            return f"Event {_id} is update"
    
    def delete(self, _id: str) -> Event:
        if _id not in self._storage:
            return EventStorageException(f"Event {_id} is not found")
        else:
            del self._storage[_id]