from utils.eventstorage import EventStorage
from models.event import Event

eventstorage = EventStorage()

class DBException(Exception):
    def __init__(self, message):
        self.message = message
    
    def to_dict(self):
        return {"Error": self.message}

class EventDB:
    def __init__(self):
        self._storage = eventstorage
    
    def create(self, event: Event) -> str:
        try:
            return self._storage.create(event)
        except Exception as ex:
            return DBException(f"{ex}: Failed CREATE event")
    
    def read(self, _id: str) -> str:
        try:
            return self._storage.read(_id)
        except DBException as ex:
            error = ex(f"{ex}: Failed READ event")
            return ex.to_dict()
    
    def list(self) ->  str:
        try:
            return self._storage.list()
        except Exception as ex:
            return DBException(f"{ex}: Failed LIST event")
            
    
    def update(self, _id: str, event: Event) -> str:
        try:
            return self._storage.update(_id, event)
        except Exception as ex:
            return DBException(f"{ex}: Failed UPDATE event")
        
    def delete(self, _id: str) -> str:
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            return DBException(f"{ex}: Failed DELETE event")