from utils.eventstorage import EventStorage
from models.event import Event

eventstorage = EventStorage()

class DBException(Exception):
    pass

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
        except Exception as ex:
            return DBException(f"{ex}: Failed READ event")
    
    def update(self, _id: str, event: Event) -> str:
        try:
            return self._storage.update(_id, event)
        except Exception as ex:
            return DBException(f"{ex}: Failed UPDATE event")
    
    