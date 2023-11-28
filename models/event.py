import datetime

class Event:
    def __init__(self, _id: str, date: str, title: str, desc: str):
        self.id = _id
        self.date = date if date else datetime.datetime.now()
        self.title = title
        self.description = desc