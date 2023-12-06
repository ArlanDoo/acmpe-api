import datetime

class Event:
    def __init__(self, _id: str, date: str, title: str, desc: str):
        self.id = _id if _id else "0"
        self.date = str(datetime.datetime.strptime(date, "%Y-%m-%d"))
        self.title = title
        self.description = desc