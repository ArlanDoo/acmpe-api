import datetime

class Event:
    def __init__(self, _id: str, date: str, title: str, desc: str):
        self.id = _id
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.title = title
        self.description = desc