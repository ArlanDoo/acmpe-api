from models.event import Event
from utils.valid_utils import len_more_then

class EventStorageException(Exception):
    pass

class EventStorage:
    def __init__(self):
        self.counter = 0
        self._storage = {}
    
    def create(self, event: Event) -> str:
        if len_more_then(event.title, 30):
            return EventStorageException(f"Title length more then 30 symbol")
        elif len_more_then(event.description, 200):
            return EventStorageException(f"Description length more then 200 symbol")
        else:
            self.counter += 1
            event.id = str(self.counter)
            self._storage[event.id] = event
            
            return f"Event {event.id} created"
    
    def read(self, _id: str) -> Event:
        if _id not in self._storage:
            return EventStorageException(f"Event {_id} is not found")
        else:
            return str(self._storage[_id])
    
    def update(self, _id: str, event: Event) -> Event:
        if _id not in self._storage:
            return EventStorageException(f"Event {_id} is not found")
        else:
            self._storage[_id] = event
            return f"Event {_id} is update"