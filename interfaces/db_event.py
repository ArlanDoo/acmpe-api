from models.event import Event
from interfaces.storage_event import EventStorage

class EventsStorageDBException(Exception):
    def __init__(self, message):
        self.message = message
    
    def to_dict(self):
        return {"error": self.message}

class EventsStorageDB:
    def __init__(self):
        self.storage = EventStorage()
    
    def create(self, event_data: Event) -> dict:
        try:
            return self.storage.create(event_data)
        except EventsStorageDBException as error:
            return error(f"Failed to create an event")
    
    def list(self):
        try:
            return self.storage.list()
        except EventsStorageDBException as error:
            return error(f"Failed to get a list of events")
    
    def read(self, _id_: str) -> dict:
        try:
            return self.storage.read(_id_)
        except EventsStorageDBException as error:
            return error(f"Event number {_id_} could not be received")
    
    def update(self, _id_: str, event_data: dict) -> dict:
        try:
            return self.storage.update(_id_, event_data)
        except EventsStorageDBException as error:
            return error(f"Event number {_id_} could not be updated")
    
    def delete(self, _id_: str) -> dict:
        try:
            return self.storage.delete(_id_)
        except EventsStorageDBException as error:
            return error(f"Event number {_id_} could not be deleted")